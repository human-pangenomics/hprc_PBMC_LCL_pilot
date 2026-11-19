#!/usr/bin/env python3
"""Build per-technology PBMC + LCL pilot data tables with the same columns as
human-pangenomics/R3_HPRC sequence_data/*.csv.

Sources are the pilot QC outputs in /private/nanopore2/hprc/data/lcl_blood_comp/qc,
the ssds upload logs (S3 paths), the Y7 HiFi data tables in HPRC_metadata and the
GTAC TruPath delivery. Run from anywhere; writes next to this script.
"""
import csv, glob, gzip, os, re, sys
from collections import defaultdict

OUT = os.path.dirname(os.path.abspath(__file__))
R3 = sys.argv[1] if len(sys.argv) > 1 else None   # path to R3_HPRC/sequence_data (for headers)
QC = '/private/nanopore2/hprc/data/lcl_blood_comp/qc'
LBC = '/private/nanopore2/hprc/data/lcl_blood_comp'
META = '/private/nanopore/hprc_qc/HPRC_metadata/submissions'
TP = '/private/nanopore2/seq_tech_center/hprc_trupath'
GENOME = 3.3e9
STUDY, BIOPROJECT = 'SRP305758', 'PRJNA701308'
UW = ('University of Washington', 'kmiyamot@uw.edu')
WUSTL = ('Washington University', 'tgraves@wustl.edu')
UCSC = ('University of California Santa Cruz', 'iviolich@ucsc.edu')
SAMPLES = ['HG08434', 'HG08435', 'HG08436', 'HG08441', 'HG08443',
           'HG08444', 'HG08446', 'HG08449', 'HG08463', 'HG08464']
UW_SAMPLES = SAMPLES[:5]


def header(name):
    with open(os.path.join(R3, name)) as f:
        return next(csv.reader(f))


def write(name, cols, rows):
    path = os.path.join(OUT, name)
    with open(path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction='raise')
        w.writeheader()
        for r in sorted(rows, key=lambda r: (r['sample_id'], r['filename'])):
            w.writerow({c: r.get(c, '') for c in cols})
    print(f'{name}: {len(rows)} rows')


def cov(bp):
    return f'{bp / GENOME:.2f}'


def read_csv(path, delim=','):
    with open(path) as f:
        return list(csv.DictReader(f, delimiter=delim))


# ntsm: per-file score = max score against the other files of the same sample
# (all technologies, pilot all-vs-all eval incl. Kinnex)
ntsm = defaultdict(float)
for p in glob.glob(f'{QC}/ntsm_eval_with_kinnex/analysis/*/*_ntsm_eval.tsv'):
    for r in read_csv(p, '\t'):
        if r['sample1'][:7] == r['sample2'][:7]:
            for k in ('sample1', 'sample2'):
                key = re.sub(r'_(hifi|ont|hic|kinnex)_counts\.txt$|_counts\.txt$', '', r[k])
                ntsm[key] = max(ntsm[key], float(r['score']))


def ntsm_of(key):
    return f'{ntsm[key]:.6f}' if key in ntsm else ''


# ---------------------------------------------------------------- HiFi
def hifi():
    cols = header('R3_HPRC_hifi_no_dc_map.csv')
    y7 = {}
    for t in (f'{META}/UW_HPRC_HiFi_Y7/UW_HPRC_HiFi_Y7_data_table.csv',
              f'{META}/WUSTL_HPRC_HiFi_Year7_LCL_FiberSeq/WUSTL_HPRC_HiFi_Year7_LCL_FiberSeq_data_table.csv'):
        for r in read_csv(t):
            y7[r['filename']] = r
    rows = []
    for src, sub in (('lcl', 'hifi_lcl'), ('pbmc', 'hifi_blood')):
        paths = {r['sample_id']: r['hifi_reads'] for r in read_csv(f'{QC}/{sub}/samples.csv')}
        for a in read_csv(f'{QC}/{sub}/{sub}_summary_agg.csv'):
            key = a['filename']; s = key[:7]; fn = a['bam_file']
            path = paths[key]
            if not path.startswith('s3://'):   # UW blood: local upload dir -> submission
                path = ('s3://human-pangenomics/submissions/466C0730-D59F-4438-9A02-3A5F06B6C2A0'
                        f'--UW_HPRC_HiFi_Year7_Blood/{s}/{fn}')
            if not path.endswith('.bam'):
                path = f'{path}/{fn}'
            fac = UW if s in UW_SAMPLES else WUSTL
            prod = re.search(r'--([^/]+)/', path).group(1)
            bp = int(a['total_bp'])
            r = dict(sample_id=s, filetype='bam', filename=fn, path=path,
                     production=prod, coverage=cov(bp),
                     study=STUDY, bioproject_accession=BIOPROJECT,
                     generator_facility=fac[0], generator_contact=fac[1],
                     library_strategy='WGS', library_source='GENOMIC', library_layout='single',
                     platform='PACBIO_SMRT', instrument_model='Revio',
                     total_reads=a['total_reads'], total_bp=bp, total_gbp=a['total_Gbp'],
                     mean=a['mean'], min=a['min'], max=a['max'],
                     n25=a['N25'], n50=a['N50'], n75=a['N75'],
                     quartile_25=a['quartile_25'], quartile_50=a['quartile_50'],
                     quartile_75=a['quartile_75'],
                     ntsm_score=ntsm_of(key), mm_tag=a['MM_tag'].upper())
            if src == 'lcl':
                r.update(data_type='unaligned reads with 5mC and 6mA',
                         notes='LCL; Fiber-seq')
                m = y7.get(fn, {})
                for c in ('biosample_accession', 'accession', 'library_id', 'design_description'):
                    r[c] = m.get(c, '')
            else:
                r.update(data_type='unaligned reads with 5mC', notes='PBMC')
            rows.append(r)
    write('PBMC_LCL_pilot_hifi.csv', cols, rows)


# ---------------------------------------------------------------- ONT
def ont():
    cols = header('R3_HPRC_ont.csv')
    s3 = {}
    for log in glob.glob('/private/nanopore2/seq_tech_center/hprc_yr7/*/upload_UCSC_HPRC_NANOPORE_YEAR7_pilot10*.log'):
        for m in re.finditer(r' to (s3://\S+\.bam)$', open(log).read(), re.M):
            s3[os.path.basename(m.group(1))] = m.group(1)
    rows = []
    for a in read_csv(f'{QC}/ont/ont_summary_agg.csv'):
        a = {k.strip(): (v or '').strip() for k, v in a.items() if k}
        key = a['file_name']; s = key[:7]; stem = key[8:]; fn = stem + '.bam'
        m = re.search(r'dorado([\d.]+)_supv?([\d.]+)', stem)
        dorado, sup = m.group(1), m.group(2)
        rows.append(dict(
            sample_id=s, filename=fn, filetype='bam', library_id=stem,
            library_strategy='WGS', library_source='GENOMIC', library_selection='RANDOM',
            library_layout='single', platform='OXFORD_NANOPORE', instrument_model='PromethION',
            design_description='UL sequencing using ONT-NEB method',
            data_type='unaligned reads with 5mCG_5hmCG mods',
            shear_method='no shear', size_selection='no SS', seq_kit='SQK-ULK114',
            basecaller='dorado', basecaller_version=dorado,
            basecaller_model=f'dna_r10.4.1_e8.2_400bps_sup@v{sup}',
            modbase_model=f'dna_r10.4.1_e8.2_400bps_sup@v{sup}_5mCG_5hmCG@v2',
            generator_facility=UCSC[0], generator_contact=UCSC[1],
            path=s3.get(fn, ''), ntsm_score=ntsm_of(key), n50=a['pass_read_N50'],
            total_gbp=a['pass_Gb'], coverage=f"{float(a['pass_Gb']) * 1e9 / GENOME:.2f}",
            coverage_over_100kb=a['pass_100kb+'], coverage_over_200kb=a['pass_200kb+'],
            coverage_over_300kb=a['pass_300kb+'], coverage_over_400kb=a['pass_400kb+'],
            coverage_over_500kb=a['pass_500kb+'], coverage_over_1mb=a['pass_1Mb+'],
            whales=a['pass_whales'], study=STUDY, bioproject_accession=BIOPROJECT,
            production='UCSC_HPRC_NANOPORE_YEAR7', sequencing_chemistry='R1041'))
    write('PBMC_LCL_pilot_ont.csv', cols, rows)


# ---------------------------------------------------------------- Hi-C (Omni-C)
def hic():
    cols = header('R3_HPRC_hic.csv')
    bp = {r['file_name']: int(r['total_bp']) for r in read_csv(f'{QC}/hic/hic_summary_agg.csv')}
    rows = []
    for r in read_csv(f'{QC}/hic/samples.csv'):
        key = r['sample_id']; s = key[:7]; lib = '_'.join(key.split('_')[:2])
        for rd in ('r1', 'r2'):
            fn = os.path.basename(r[rd]); half = bp[key] // 2
            rows.append(dict(
                sample_id=s, filename=fn, study=STUDY, bioproject_accession=BIOPROJECT,
                library_id=lib, library_strategy='Hi-C', library_source='GENOMIC',
                platform='ILLUMINA', instrument_model='Illumina NovaSeq 6000',
                design_description='Illumina Sequencing of Omni-C Libraries',
                generator_facility=UCSC[0], generator_contact='wseligma@ucsc.edu',
                data_type='unaligned reads', filetype='fastq', library_layout='paired',
                library_selection='RANDOM', shear_method='no shear',
                total_bp=half, coverage=cov(half), total_gbp=f'{half / 1e9:.2f}',
                ntsm_score=ntsm_of(key),
                path=('s3://human-pangenomics/submissions/192FC6C4-DDC0-45C6-ABA4-1C4FDE785008'
                      f'--WB_LCL_PILOT_OMNIC/{s}/{fn}'),
                production='WB_LCL_PILOT_OMNIC', notes='LCL'))
    write('PBMC_LCL_pilot_hic.csv', cols, rows)


# ---------------------------------------------------------------- Kinnex
def kinnex():
    cols = header('R3_HPRC_kinnex.csv')
    rows = []
    for s in SAMPLES:
        d = f'{LBC}/kinnex/upload/{s}'
        with open(f'{d}/{s}.flnc.report.csv') as f:
            next(f); first = next(f)
            n = 1 + sum(1 for _ in f)
        movie = first.split('/')[0]
        bc = re.search(r'_(bc\d+)_5p', first).group(1)
        fac = UW if s in UW_SAMPLES else WUSTL
        fn = f'{s}.flnc.bam'
        rows.append(dict(
            sample_id=s, filename=fn, total_reads=n,
            path=('s3://human-pangenomics/submissions/D7C82359-0994-4BFB-802F-70E9D873C479'
                  f'--WB_LCL_PILOT_KINNEX/{s}/{fn}'),
            title='flnc bams of PacBio HiFi iso-seq sequencing of cDNA kinnex libraries',
            study=STUDY, bioproject_accession=BIOPROJECT, library_id=f'{s}.{movie}',
            data_type='unaligned reads', filetype='bam', cell_type='lymph',
            generator_facility=fac[0], generator_contact=fac[1],
            production='WB_LCL_PILOT_KINNEX', platform_unit_1=movie, barcode=bc,
            basecaller_version='25.4.0.278749', platform='PACBIO', instrument_model='REVIO',
            ccs_algorithm='8.7.0', lima_version='2.15.99', refine_version='4.4.99',
            library_strategy='isoseq', library_source='transcriptomic', library_selection='cDNA',
            library_layout='single', shear_method='NA', size_selection='NA',
            design_description='PacBio HiFi iso-seq sequencing of cDNA kinnex libraries',
            ntsm_score=ntsm_of(f'{s}.flnc')))
    write('PBMC_LCL_pilot_kinnex.csv', cols, rows)


# ---------------------------------------------------------------- Illumina TruPath
def ill():
    cols = header('R3_HPRC_ill.csv')
    sex = {r['sample_id']: r['sex'] for r in read_csv(f'{QC}/metadata.txt', '\t')}
    rows = []
    for r in read_csv(f'{TP}/samples.tsv', '\t'):
        s = r['sample_id']
        if s not in SAMPLES:
            continue
        mm = {}
        for line in open(f"{TP}/{r['analysis_directory']}/{s}.mapping_metrics.csv"):
            p = line.rstrip('\n').split(',')
            if p[0] == 'MAPPING/ALIGNING SUMMARY' and p[1] == '':
                mm.setdefault(p[2], p[3])
        half = int(round(int(mm['Total input reads']) * float(mm['Estimated read length']) / 2))
        for rd in ('fastq_r1', 'fastq_r2'):
            fn = os.path.basename(r[rd])
            rows.append(dict(
                sample_id=s, total_bp=half, total_gbp=f'{half / 1e9:.2f}', coverage=cov(half),
                filetype='fastq', platform='ILLUMINA', instrument_model='Illumina NovaSeq X',
                library_construction_protocol='Illumina TruPath', library_layout='PAIRED',
                library_strategy='WGS', read_length=151,
                gender={'male': 1, 'female': 2}[sex[s]],
                other_comments=f"LCL; GTAC@MGI {r['delivery_id']} flowcell {r['flowcell_id']} lane {r['lane']}",
                path=('s3://human-pangenomics/submissions/23B8D27E-1D54-4A7D-B6C1-1E14E1AA51E5'
                      f'--WB_LCL_PILOT_TRUPATH/{s}/raw/{fn}'),
                filename=fn))
    write('PBMC_LCL_pilot_ill.csv', cols, rows)


# ---------------------------------------------------------------- sample tables
def samples():
    sdir = os.path.join(os.path.dirname(OUT), 'sample')
    os.makedirs(sdir, exist_ok=True)
    meta = {r['sample_id']: r for r in read_csv(f'{QC}/metadata.txt', '\t')}
    t = {k: read_csv(os.path.join(OUT, f'PBMC_LCL_pilot_{k}.csv'))
         for k in ('hifi', 'ont', 'hic', 'kinnex', 'ill')}

    def by(rows, s):
        return [r for r in rows if r['sample_id'] == s]

    def wmean(rows, val, w):   # bp-weighted mean of per-file values
        tw = sum(float(r[w]) for r in rows)
        return sum(float(r[val]) * float(r[w]) for r in rows) / tw

    def csum(rows):
        return sum(float(r['coverage']) for r in rows)

    with open(os.path.join(R3, '..', 'sample', 'R3_HPRC_metadata.csv')) as f:
        mcols = next(csv.reader(f))
    with open(os.path.join(R3, '..', 'sample', 'R3_HPRC_coverage_summary.csv')) as f:
        ccols = next(csv.reader(f))
    mrows, crows = [], []
    for s in SAMPLES:
        mrows.append(dict(sample_id=s, family_id='NaN', sex=meta[s]['sex'],
                          population_abbreviation='', production_year='YR7'))
        h, o = by(t['hifi'], s), by(t['ont'], s)
        hcov = csum(h)
        crows.append(dict(
            sample_id=s, production_year='YR7', coverage_hifi=f'{hcov:.2f}',
            deepconsensus_coverage_hifi=0, coverage_non_dc=f'{hcov:.2f}',
            coverage_mm_hifi=f"{csum([r for r in h if r['mm_tag'] == 'TRUE']):.2f}",
            hifi_prod_site=meta[s]['hifi_production_center'],
            n50_hifi=f"{wmean(h, 'n50', 'total_bp'):.2f}", phasing='hic',
            coverage_hic=f"{csum(by(t['hic'], s)):.2f}",
            coverage_ill=f"{csum(by(t['ill'], s)):.2f}",
            total_reads_kinnex=sum(int(r['total_reads']) for r in by(t['kinnex'], s)),
            coverage_ont=f'{csum(o):.2f}',
            coverage_100kb_ont=f"{sum(float(r['coverage_over_100kb']) for r in o):.2f}",
            read_N50_ont=round(wmean(o, 'n50', 'total_gbp')),
            sequencing_chemistry_ont='R1041',
            notes='PBMC + LCL pilot; HiFi = LCL (Fiber-seq) + PBMC; Illumina = TruPath'))
    for name, cols, rows in (('PBMC_LCL_pilot_metadata.csv', mcols, mrows),
                             ('PBMC_LCL_pilot_coverage_summary.csv', ccols, crows)):
        with open(os.path.join(sdir, name), 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=cols)
            w.writeheader(); w.writerows(rows)
        print(f'sample/{name}: {len(rows)} rows')


if __name__ == '__main__':
    hifi(); ont(); hic(); kinnex(); ill(); samples()
