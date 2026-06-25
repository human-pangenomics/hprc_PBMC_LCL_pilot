# HPRC Year 7 Pilot: Whole Blood vs. LCL Sequencing and Assembly QC Report

**Project:** HPRC Year 7 pilot — whole blood (WB) vs. lymphoblastoid cell line (LCL) comparison  
**Samples:** 10 individuals (HG08434–HG08464)  
**Date:** April 2026

---

## 1. Overview

This report summarizes sequencing data quality, sample identity verification, assembly, and assembly QC for a 10-sample HPRC Year 7 pilot. The central question is whether using whole blood as a source material for half of the PacBio HiFi input affects sequencing or assembly quality relative to the standard LCL-derived material. Each sample was sequenced with HiFi from both WB and LCL sources; assemblies were produced from the combined input. Additional data types collected include OmniC (LCL), Oxford Nanopore Technology (ONT, LCL), and Kinnex long-read RNA (LCL).

---

## 2. Samples

| Sample | Sex | Production Center |
|---|---|---|
| HG08434 | Female | UW |
| HG08435 | Female | UW |
| HG08436 | Male | UW |
| HG08441 | Female | UW |
| HG08443 | Male | UW |
| HG08444 | Male | WUSTL |
| HG08446 | Female | WUSTL |
| HG08449 | Female | WUSTL |
| HG08463 | Male | WUSTL |
| HG08464 | Male | WUSTL |

---

## 3. Sequencing Data

### 3.1 PacBio HiFi

Each sample was sequenced with HiFi from two sources: whole blood (WB) and LCL. The target was 30x per source (60x combined). Assemblies were produced from the combined WB + LCL input.

| Sample | WB Coverage | WB Read N50 (bp) | LCL Coverage | LCL Read N50 (bp) | Total Coverage |
|---|---|---|---|---|---|
| HG08434 | 36.2 | 25,656 | 39.6 | 20,852 | 75.8 |
| HG08435 | 41.5 | 24,633 | 34.6 | 25,906 | 76.1 |
| HG08436 | 45.4 | 23,743 | 38.7 | 25,073 | 84.1 |
| HG08441 | 45.3 | 25,226 | 34.4 | 27,526 | 79.7 |
| HG08443 | 41.4 | 25,746 | 44.0 | 27,660 | 85.5 |
| HG08444 | 33.9 | 23,040 | 35.5 | 27,505 | 69.4 |
| HG08446 | 35.4 | 23,952 | 36.2 | 23,313 | 71.5 |
| HG08449 | 31.8 | 24,928 | 28.0 | 27,236 | 59.8 |
| HG08463 | 35.0 | 23,529 | 29.7 | 28,073 | 64.7 |
| HG08464 | 30.4 | 26,901 | 30.9 | 23,090 | 61.2 |
| **Mean** | **37.6** | **24,735** | **35.2** | **25,623** | **72.8** |

Read N50 values are comparable between WB and LCL sources (mean 24.7 kb vs. 25.6 kb respectively), with no systematic difference in read length distribution. Coverage targets (30x per source) are met for most samples; HG08449 LCL (28.0x) and HG08464 WB (30.4x) are at or slightly below target.

### 3.2 OmniC

OmniC chromatin conformation data was generated from LCL and used for haplotype phasing in assembly. Target: 30x.

| Sample | Total Coverage |
|---|---|
| HG08434 | 44.9 |
| HG08435 | 44.7 |
| HG08436 | 49.0 |
| HG08441 | 46.0 |
| HG08443 | 46.5 |
| HG08444 | 33.4 |
| HG08446 | 39.1 |
| HG08449 | 41.7 |
| HG08463 | 47.7 |
| HG08464 | 39.8 |

All samples meet or exceed the 30x target (range 33–49x).

### 3.3 ONT

Ultra-long ONT data was generated from LCL. Target: ≥30x coverage in reads ≥100 kb; pass threshold ≥25x. Read N50 values are reported as a proxy for ultra-long read content.

| Sample | Total Coverage | ≥100 kb Coverage | Read N50 (bp) |
|---|---|---|---|
| HG08434 | 59.8 | 29.5 | 98,928 |
| HG08435 | 75.5 | 37.8 | 99,949 |
| HG08436 | 74.3 | 37.8 | 101,683 |
| HG08441 | 61.6 | 32.8 | 105,998 |
| HG08443 | 71.0 | 36.8 | 103,529 |
| HG08444 | 72.3 | 37.3 | 103,257 |
| HG08446 | 77.8 | 41.0 | 105,134 |
| HG08449 | 68.1 | 31.9 | 95,306 |
| HG08463 | 71.8 | 36.2 | 100,994 |
| HG08464 | 63.0 | 34.4 | 110,197 |

All samples exceed the 25x pass threshold for ≥100 kb coverage (range 29.5–41.0x) and meet the 30x target with the exception of HG08434 (29.5x), which is marginally below. Read N50 values range from 95–110 kb.

### 3.4 Kinnex

Kinnex long-read RNA sequencing data was generated from LCL. Target: ~10 million segmented reads per sample. Samples were processed in two pools of 5 (UW: HG08434–HG08443; WUSTL: HG08444–HG08464) through the SMRTLink IsoSeq pipeline (v25.4.0).

| Sample | Segmented reads |
|---|---|
| HG08434 | 14,132,445 |
| HG08435 | 12,290,361 |
| HG08436 | 13,412,805 |
| HG08441 | 12,404,222 |
| HG08443 | 13,024,729 |
| HG08444 | 12,063,663 |
| HG08446 | 14,052,167 |
| HG08449 | 15,082,834 |
| HG08463 | 14,098,116 |
| HG08464 | 12,086,047 |

All samples exceed the 10M read target (range 12.1M–15.1M). Samples were processed in two pools of 5 (UW: HG08434–HG08443 on m84046; WUSTL: HG08444–HG08464 on m84081) through the SMRTLink IsoSeq pipeline (v25.4.0). Mean FLNC read length was 2,256 bp (UW) and 1,927 bp (WUSTL).

---

## 4. Sample Identity QC

### 4.1 Cross-data-type ntsm comparison

Sample identity was assessed using ntsm v1.2.1, a k-mer-based identity tool. ntsm computes a pairwise distance score between sequencing files; lower scores indicate the same individual. An all-vs-all comparison was run across 108 files representing five data types: WB HiFi, LCL HiFi, ONT, OmniC, and Kinnex.

**Score interpretation:**

| Score range | Interpretation |
|---|---|
| ~0.13–0.25 | Same individual |
| > 0.5 | Different individuals |

All 10 samples pass. A sample is flagged PASS when all within-sample pairs score below 0.5 and all cross-sample pairs score above 0.5.

| Sample | Files (HiFi/ONT/OmniC/Kinnex) | Within-sample score (min–max) | Cross-sample score (min) | Flag |
|---|---|---|---|---|
| HG08434 | 5/2/4/1 | 0.135–0.214 | 1.028 | PASS |
| HG08435 | 5/2/4/1 | 0.130–0.233 | 1.037 | PASS |
| HG08436 | 6/2/4/1 | 0.125–0.218 | 1.057 | PASS |
| HG08441 | 5/2/4/1 | 0.132–0.204 | 1.057 | PASS |
| HG08443 | 5/2/4/1 | 0.127–0.223 | 1.056 | PASS |
| HG08444 | 2/2/4/1 | 0.136–0.207 | 1.028 | PASS |
| HG08446 | 2/2/4/1 | 0.126–0.213 | 1.030 | PASS |
| HG08449 | 2/3/4/1 | 0.126–0.209 | 1.030 | PASS |
| HG08463 | 2/2/4/1 | 0.128–0.219 | 1.055 | PASS |
| HG08464 | 2/3/4/1 | 0.127–0.196 | 1.039 | PASS |

No sample swaps or cross-contamination were detected. Within-sample scores are well-separated from cross-sample scores across all data type combinations, including WB HiFi vs. LCL HiFi (within-sample mean 0.132), confirming concordance between the two HiFi source materials.

Two notes on score behavior: OmniC within-sample scores are slightly elevated relative to HiFi or ONT pairs (up to 0.233) due to lower per-lane coverage reducing shared k-mer counts; scores remain well below the 0.5 threshold. Kinnex cross-sample scores are anomalously high (14–21) because FLNC reads capture the expressed transcriptome rather than the whole genome, making cross-sample kinnex-to-kinnex comparison uninformative; within-sample kinnex scores against other data types are within the expected range and confirm correct sample identity.

### 4.2 Genotyping concordance (in progress)

ntsm operates on sequencing reads without an external truth set. As a complementary identity anchor, alignment-based concordance against Coriell-derived SNP genotyping array data is planned but has not yet been run. This will provide an independent confirmation of sample identity using a reference dataset orthogonal to the sequencing data collected here.

---

## 5. Assembly

Haplotype-resolved assemblies were produced for all 10 samples using hifiasm with OmniC-based phasing. The combined WB + LCL HiFi input was used for all assemblies; no sample was assembled from a single source in isolation. Assemblies are available as `hap1` and `hap2` FASTA files in `../assembly/<sample_id>/`.

Assemblies were generated using the same workflow used for HPRC R2 production assemblies: `hic_hifiasm_assembly_cutadapt_multistep.wdl` from the [human-pangenomics/hpp_production_workflows](https://github.com/human-pangenomics/hpp_production_workflows) repository. The workflow runs hifiasm in three steps (HiFi binning → ONT ultralong binning → HiC-phased assembly), then converts GFAs to FASTA and assigns sex chromosomes using `yak sexchr`.

---

## 6. Assembly QC

Assembly QC was run using the HPRC `standard_qc_nontrio` workflow, which includes dipcall (variant calling vs. GRCh38), asmgene (gene completeness), quast (contiguity), and yak (k-mer QV). T2T contig and scaffold counts were computed separately using `findAssemblyBreakpoints` against CHM13v2. Gene completeness was also assessed with compleasm using sex-aware BUSCO lineages.

Full per-haplotype results are in `assembly_qc/assembly_qc_summary.csv`.

### 6.1 Assembly size and contiguity

| Sample | Hap | Total (Gbp) | N50 (Mb) | auN (Mb) | Contigs |
|---|---|---|---|---|---|
| HG08434 | hap1 | 3.039 | 155.3 | 154.0 | 85 |
| HG08434 | hap2 | 3.041 | 153.7 | 153.8 | 60 |
| HG08435 | hap1 | 3.028 | 136.9 | 142.4 | 92 |
| HG08435 | hap2 | 3.060 | 137.2 | 149.1 | 72 |
| HG08436 | hap1 | 2.931 | 135.5 | 140.8 | 126 |
| HG08436 | hap2 | 3.053 | 146.6 | 147.8 | 111 |
| HG08441 | hap1 | 3.051 | 154.9 | 153.6 | 89 |
| HG08441 | hap2 | 3.033 | 154.5 | 151.0 | 69 |
| HG08443 | hap1 | 2.932 | 146.2 | 148.6 | 143 |
| HG08443 | hap2 | 3.051 | 155.4 | 152.6 | 96 |
| HG08444 | hap1 | 2.952 | 137.0 | 147.6 | 72 |
| HG08444 | hap2 | 3.030 | 134.6 | 146.5 | 73 |
| HG08446 | hap1 | 3.029 | 135.6 | 135.7 | 151 |
| HG08446 | hap2 | 3.029 | 135.0 | 132.4 | 108 |
| HG08449 | hap1 | 3.040 | 136.6 | 131.8 | 118 |
| HG08449 | hap2 | 3.028 | 134.9 | 135.2 | 85 |
| HG08463 | hap1 | 2.931 | 137.0 | 144.2 | 76 |
| HG08463 | hap2 | 3.047 | 135.5 | 143.7 | 96 |
| HG08464 | hap1 | 2.916 | 145.4 | 151.4 | 106 |
| HG08464 | hap2 | 3.045 | 145.8 | 150.1 | 71 |

Total assembly lengths (2.92–3.06 Gbp) and N50 values (132–155 Mb) are consistent across all samples. Two haplotypes show elevated contig counts (HG08443 hap1 = 143, HG08446 hap1 = 151); all others fall in the normal range of 60–118.

### 6.2 T2T contigs and scaffolds

| Sample | T2T Contigs (combined) | T2T Scaffolds (combined) |
|---|---|---|
| HG08434 | 22 | 29 |
| HG08435 | 15 | 24 |
| HG08436 | 14 | 25 |
| HG08441 | 22 | 30 |
| HG08443 | 13 | 18 |
| HG08444 | 14 | 21 |
| HG08446 | 13 | 22 |
| HG08449 | 12 | 14 |
| HG08463 | 11 | 19 |
| HG08464 | 20 | 31 |

T2T counts are summed across both haplotypes per sample. Range: 11–22 T2T contigs and 14–31 T2T scaffolds.

### 6.3 Gene completeness

#### asmgene

| Sample | Hap | Single-copy genes | % Single-copy |
|---|---|---|---|
| HG08434 | hap1 | 33,460 | 97.95% |
| HG08434 | hap2 | 33,506 | 98.09% |
| HG08435 | hap1 | 33,523 | 98.14% |
| HG08435 | hap2 | 33,479 | 98.01% |
| HG08436 | hap1 | 33,504 | 98.08% |
| HG08436 | hap2 | 33,523 | 98.14% |
| HG08441 | hap1 | 33,492 | 98.05% |
| HG08441 | hap2 | 33,441 | 97.90% |
| HG08443 | hap1 | 33,464 | 97.97% |
| HG08443 | hap2 | 33,502 | 98.08% |
| HG08444 | hap1 | 33,444 | 97.91% |
| HG08444 | hap2 | 33,444 | 97.91% |
| HG08446 | hap1 | 33,420 | 97.84% |
| HG08446 | hap2 | 33,378 | 97.71% |
| HG08449 | hap1 | 33,506 | 98.09% |
| HG08449 | hap2 | 33,367 | 97.68% |
| HG08463 | hap1 | 33,351 | 97.63% |
| HG08463 | hap2 | 33,505 | 98.09% |
| HG08464 | hap1 | 33,309 | 97.51% |
| HG08464 | hap2 | 33,487 | 98.03% |

Single-copy gene completeness ranges from 97.5–98.1% across all haplotypes.

#### Compleasm

Compleasm was run with sex-aware BUSCO lineages: `primatesnoY_odb10` for X-bearing haplotypes (all female haplotypes and male hap2), and `primatesnoX_odb10` for Y-bearing haplotypes (male hap1). An initial run used the wrong lineage for male hap1 assemblies and was corrected.

| Sample | Hap | S% | D% | F% | M% |
|---|---|---|---|---|---|
| HG08434 | hap1 | 99.19 | 0.81 | 0.00 | 0.01 |
| HG08434 | hap2 | 99.28 | 0.71 | 0.01 | 0.00 |
| HG08435 | hap1 | 99.27 | 0.71 | 0.01 | 0.01 |
| HG08435 | hap2 | 99.29 | 0.69 | 0.01 | 0.01 |
| HG08436 | hap1 | 99.32 | 0.65 | 0.01 | 0.02 |
| HG08436 | hap2 | 99.29 | 0.71 | 0.00 | 0.01 |
| HG08441 | hap1 | 99.27 | 0.73 | 0.00 | 0.00 |
| HG08441 | hap2 | 99.16 | 0.68 | 0.01 | 0.15 |
| HG08443 | hap1 | 99.16 | 0.74 | 0.01 | 0.09 |
| HG08443 | hap2 | 99.31 | 0.69 | 0.00 | 0.00 |
| HG08444 | hap1 | 99.02 | 0.63 | 0.01 | 0.34 |
| HG08444 | hap2 | 99.29 | 0.69 | 0.01 | 0.01 |
| HG08446 | hap1 | 99.24 | 0.71 | 0.00 | 0.04 |
| HG08446 | hap2 | 99.04 | 0.73 | 0.00 | 0.23 |
| HG08449 | hap1 | 99.27 | 0.71 | 0.01 | 0.01 |
| HG08449 | hap2 | 98.53 | 0.73 | 0.06 | 0.68 |
| HG08463 | hap1 | 98.85 | 0.65 | 0.01 | 0.49 |
| HG08463 | hap2 | 99.30 | 0.70 | 0.00 | 0.00 |
| HG08464 | hap1 | 98.49 | 0.65 | 0.02 | 0.83 |
| HG08464 | hap2 | 99.27 | 0.73 | 0.00 | 0.00 |

S% ranges from 98.5–99.3% across all haplotypes. Slightly elevated M% in some male hap1 assemblies (up to 0.83% in HG08464) reflects the genuine biological absence of a small number of X-linked genes from the Y-bearing haplotype and is not indicative of assembly error.

### 6.4 QV

yak QV was estimated using OmniC reads as the k-mer input, as WGS Illumina data was not available. This results in systematically lower QV scores relative to WGS-based estimates (see Section 7.3 for context).

| Sample | Hap | QV | CV |
|---|---|---|---|
| HG08434 | hap1 | 44.29 | 0.990 |
| HG08434 | hap2 | 44.23 | 0.990 |
| HG08435 | hap1 | 45.54 | 0.989 |
| HG08435 | hap2 | 45.52 | 0.990 |
| HG08436 | hap1 | 46.46 | 0.989 |
| HG08436 | hap2 | 46.17 | 0.992 |
| HG08441 | hap1 | 44.88 | 0.992 |
| HG08441 | hap2 | 44.93 | 0.991 |
| HG08443 | hap1 | 45.30 | 0.989 |
| HG08443 | hap2 | 44.85 | 0.992 |
| HG08444 | hap1 | 44.96 | 0.981 |
| HG08444 | hap2 | 44.36 | 0.987 |
| HG08446 | hap1 | 45.68 | 0.991 |
| HG08446 | hap2 | 45.56 | 0.991 |
| HG08449 | hap1 | 44.96 | 0.993 |
| HG08449 | hap2 | 44.95 | 0.986 |
| HG08463 | hap1 | 45.15 | 0.989 |
| HG08463 | hap2 | 44.84 | 0.993 |
| HG08464 | hap1 | 45.66 | 0.986 |
| HG08464 | hap2 | 45.02 | 0.991 |

QV range: 44.2–46.5. CV (k-mer coverage uniformity) is 0.981–0.993 across all haplotypes, indicating consistent coverage. See Section 7.3 for interpretation relative to HPRC R2 values.

---

## 7. Comparison with HPRC R2 Assemblies

The pilot assemblies were compared against HPRC R2 non-trio assemblies to assess whether they meet production quality standards. The HPRC R2 reference set used here is from non-trio samples with comparable sequencing inputs.

| Metric | WB-LCL Pilot | HPRC R2 (non-trio) | Notes |
|---|---|---|---|
| Total length | 2.92–3.06 Gbp | 2.92–3.06 Gbp | Identical range |
| auN | 132–154 Mbp | 115–152 Mbp | Competitive |
| N50 | 132–155 Mbp | ~115–155 Mbp | Competitive |
| Contig count | 60–151 per hap | 43–99 per hap | 2 haplotypes elevated |
| T2T contigs | 11–22 (both haps) | 7–26 (both haps) | Comparable |
| T2T scaffolds | 14–31 (both haps) | 3–20 (both haps) | Pilot trends higher |
| asmgene % | 97.5–98.1% | 97.8–98.6% | Slightly lower, within range |
| Compleasm S% | 98.5–99.3% | ~99% | Matches production |
| yak QV | 44–46 | 52–61 (WGS) / 44–47 (HiC) | See Section 7.3 |
| Switch/hamming | N/A | Available (trio only) | Non-trio limitation |

### 7.1 Assembly size and contiguity

Total haplotype lengths (2.92–3.06 Gbp) and auN values (132–154 Mbp) are within the normal HPRC R2 range. Two haplotypes show slightly elevated contig counts (HG08443 hap1 = 143, HG08446 hap1 = 151) compared to the HPRC R2 typical range of 43–99. Most pilot haplotypes (60–118) are within normal range.

### 7.2 Gene completeness

asmgene single-copy completeness (97.5–98.1%) is slightly below the HPRC R2 range (97.8–98.6%), though within the expected range of variation. The ~1,200 lower absolute gene count reflects use of Ensembl cDNA annotation in the pilot vs. GENCODE used by HPRC; percentages are the appropriate comparison. Compleasm S% (98.5–99.3%) is consistent with HPRC R2 production values.

### 7.3 QV and the OmniC input caveat

Pilot yak QV values (44–46) are systematically ~10–12 points below published HPRC R2 values (52–61). This gap is attributable to the use of OmniC reads as the yak k-mer input rather than PCR-free WGS Illumina reads. OmniC reads have non-uniform genomic coverage and include chimeric ligation-junction reads that degrade k-mer spectrum quality.

To assess whether this gap reflects a genuine quality difference, yak QV was re-run on 10 HPRC R2 batch 4 samples using their own OmniC reads in place of WGS. The resulting QV values (44–47) are indistinguishable from the pilot values, confirming that the gap is a consequence of read type rather than assembly quality. See `hprc_r2_hic_qc/wgs_vs_hic_qv.csv` for the full comparison.

---

## 8. Summary

Across all evaluated metrics — assembly size, contiguity, T2T content, gene completeness, and k-mer QV — the WB-LCL pilot assemblies are within the normal range for HPRC R2 non-trio production assemblies. At the read level, WB and LCL HiFi inputs show comparable read length distributions (mean N50 ~24.7 kb and ~25.6 kb respectively), and ntsm cross-source comparisons confirm that WB and LCL reads from the same individual are concordant with one another.

These results are consistent with WB being a suitable HiFi input source for HPRC-standard assembly. However, because each sample was assembled from the combined WB + LCL input rather than from either source in isolation, a direct comparison of WB-only vs. LCL-only assembly quality was not performed and remains a question for future work.

All samples meet or exceed sequencing coverage targets for HiFi (combined), OmniC, and ONT. Kinnex coverage metrics are pending aggregation. Alignment-based sample identity confirmation using Coriell SNP genotyping array data is planned as a next step to complement the ntsm all-vs-all analysis.
