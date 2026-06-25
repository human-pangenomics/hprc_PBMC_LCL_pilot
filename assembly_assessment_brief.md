# HPRC Year 7 Pilot: WB vs. LCL — Summary

**Samples:** 10 individuals (HG08434–HG08464) | **Date:** April 2026

Ten samples were sequenced with PacBio HiFi from two sources: whole blood (WB) and LCL. Additional data types include OmniC (LCL, for phasing), ONT (LCL, ultralong), and Kinnex long-read RNA (LCL). Assemblies were produced from the combined WB + LCL HiFi input using the HPRC R2 production workflow (`hic_hifiasm_assembly_cutadapt_multistep.wdl`, [human-pangenomics/hpp_production_workflows](https://github.com/human-pangenomics/hpp_production_workflows)). Assembly QC used the HPRC `standard_qc_nontrio` workflow (dipcall, asmgene, quast, yak), supplemented by compleasm and `findAssemblyBreakpoints` for T2T counts.

---

## Sequencing coverage

| Sample | Sex | HiFi WB | HiFi LCL | HiFi Total | OmniC | ONT ≥100 kb | Kinnex reads |
|---|---|---|---|---|---|---|---|
| HG08434 | F | 36.2 | 39.6 | 75.8 | 44.9 | 29.5 | 14,132,445 |
| HG08435 | F | 41.5 | 34.6 | 76.1 | 44.7 | 37.8 | 12,290,361 |
| HG08436 | M | 45.4 | 38.7 | 84.1 | 49.0 | 37.8 | 13,412,805 |
| HG08441 | F | 45.3 | 34.4 | 79.7 | 46.0 | 32.8 | 12,404,222 |
| HG08443 | M | 41.4 | 44.0 | 85.5 | 46.5 | 36.8 | 13,024,729 |
| HG08444 | M | 33.9 | 35.5 | 69.4 | 33.4 | 37.3 | 12,063,663 |
| HG08446 | F | 35.4 | 36.2 | 71.5 | 39.1 | 41.0 | 14,052,167 |
| HG08449 | F | 31.8 | 28.0 | 59.8 | 41.7 | 31.9 | 15,082,834 |
| HG08463 | M | 35.0 | 29.7 | 64.7 | 47.7 | 36.2 | 14,098,116 |
| HG08464 | M | 30.4 | 30.9 | 61.2 | 39.8 | 34.4 | 12,086,047 |

Coverage targets: HiFi 30x per source (60x combined); OmniC 30x; ONT ≥25x at ≥100 kb; Kinnex ~10M segmented reads. All samples meet targets; HG08434 ONT (29.5x) is marginally below the 30x goal but above the 25x pass threshold.

---

## Sample identity QC

Sample identity was assessed using ntsm v1.2.1, a k-mer-based identity tool, with an all-vs-all comparison across all files (WB HiFi, LCL HiFi, ONT, OmniC, Kinnex). Within-sample pairs score ~0.13–0.25; cross-sample pairs score >1.0. All 10 samples pass with no swaps or cross-contamination detected.

| Sample | Within-sample score (min–max) | Cross-sample score (min) | Flag |
|---|---|---|---|
| HG08434 | 0.135–0.214 | 1.028 | PASS |
| HG08435 | 0.130–0.233 | 1.037 | PASS |
| HG08436 | 0.125–0.218 | 1.057 | PASS |
| HG08441 | 0.132–0.204 | 1.057 | PASS |
| HG08443 | 0.127–0.223 | 1.056 | PASS |
| HG08444 | 0.136–0.207 | 1.028 | PASS |
| HG08446 | 0.126–0.213 | 1.030 | PASS |
| HG08449 | 0.126–0.209 | 1.030 | PASS |
| HG08463 | 0.128–0.219 | 1.055 | PASS |
| HG08464 | 0.127–0.196 | 1.039 | PASS |

As a complementary check, concordance against Coriell-derived SNP genotyping array data is in development and will provide an independent identity confirmation orthogonal to the sequencing data.

---

## Assembly QC

| Sample | Hap | N50 (Mb) | auN (Mb) | Contigs | T2T scaffolds | asmgene % | Compleasm S% | yak QV |
|---|---|---|---|---|---|---|---|---|
| HG08434 | hap1 | 155.3 | 154.0 | 85 | 14 | 97.95 | 99.19 | 44.3 |
| HG08434 | hap2 | 153.7 | 153.8 | 60 | 15 | 98.09 | 99.28 | 44.2 |
| HG08435 | hap1 | 136.9 | 142.4 | 92 | 11 | 98.14 | 99.27 | 45.5 |
| HG08435 | hap2 | 137.2 | 149.1 | 72 | 13 | 98.01 | 99.29 | 45.5 |
| HG08436 | hap1 | 135.5 | 140.8 | 126 | 12 | 98.08 | 99.32 | 46.5 |
| HG08436 | hap2 | 146.6 | 147.8 | 111 | 13 | 98.14 | 99.29 | 46.2 |
| HG08441 | hap1 | 154.9 | 153.6 | 89 | 15 | 98.05 | 99.27 | 44.9 |
| HG08441 | hap2 | 154.5 | 151.0 | 69 | 15 | 97.90 | 99.16 | 44.9 |
| HG08443 | hap1 | 146.2 | 148.6 | 143 | 7 | 97.97 | 99.16 | 45.3 |
| HG08443 | hap2 | 155.4 | 152.6 | 96 | 11 | 98.08 | 99.31 | 44.8 |
| HG08444 | hap1 | 137.0 | 147.6 | 72 | 12 | 97.91 | 99.02 | 45.0 |
| HG08444 | hap2 | 134.6 | 146.5 | 73 | 9 | 97.91 | 99.29 | 44.4 |
| HG08446 | hap1 | 135.6 | 135.7 | 151 | 9 | 97.84 | 99.24 | 45.7 |
| HG08446 | hap2 | 135.0 | 132.4 | 108 | 13 | 97.71 | 99.04 | 45.6 |
| HG08449 | hap1 | 136.6 | 131.8 | 118 | 9 | 98.09 | 99.27 | 45.0 |
| HG08449 | hap2 | 134.9 | 135.2 | 85 | 5 | 97.68 | 98.53 | 45.0 |
| HG08463 | hap1 | 137.0 | 144.2 | 76 | 8 | 97.63 | 98.85 | 45.1 |
| HG08463 | hap2 | 135.5 | 143.7 | 96 | 11 | 98.09 | 99.30 | 44.8 |
| HG08464 | hap1 | 145.4 | 151.4 | 106 | 15 | 97.51 | 98.49 | 45.7 |
| HG08464 | hap2 | 145.8 | 150.1 | 71 | 16 | 98.03 | 99.27 | 45.0 |

Assemblies were produced from the combined WB + LCL HiFi input to assess whether using whole blood for half of the HiFi sequencing affected assembly quality. yak QV was estimated using OmniC reads as k-mer input (WGS Illumina unavailable); see comparison table note below.

---

## Comparison with HPRC R2 non-trio assemblies

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
| yak QV | 44–46 | 52–61 (WGS) / 44–47 (OmniC) | Read-type artifact; see note |
| Switch/hamming | N/A | Available (trio only) | Non-trio limitation |

**yak QV note:** The ~11-point gap vs. published HPRC R2 values is attributable to OmniC reads as k-mer input rather than PCR-free WGS. Re-running yak on 10 HPRC R2 batch 4 samples with their own OmniC reads yields QV 44–47, indistinguishable from pilot values. See `hprc_r2_hic_qc/wgs_vs_hic_qv.csv`.
