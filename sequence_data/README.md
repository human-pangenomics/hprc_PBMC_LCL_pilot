# Pilot sequence data tables

Working tables for the PBMC + LCL pilot, laid out like the
[R3_HPRC](https://github.com/human-pangenomics/R3_HPRC) `sequence_data/` and `sample/` tables so the
same scripts can read them. Table names follow R3 with a `PBMC_LCL_pilot_` prefix, and every column
keeps its R3 name and order. Only columns with known, final values are included (sample, S3 path,
size/coverage stats, ntsm). Submission metadata such as accessions, library and instrument fields
is left out because it is not finalized yet.

| Table | R3 equivalent | Rows |
|---|---|---|
| `sequence_data/PBMC_LCL_pilot_hifi_no_dc_map.csv` | `R3_HPRC_hifi_no_dc_map.csv` | 36 (18 LCL Fiber-seq + 18 PBMC) |
| `sequence_data/PBMC_LCL_pilot_ont.csv` | `R3_HPRC_ont.csv` | 22 |
| `sequence_data/PBMC_LCL_pilot_hic.csv` | `R3_HPRC_hic.csv` | 80 (R1 and R2) |
| `sequence_data/PBMC_LCL_pilot_kinnex.csv` | `R3_HPRC_kinnex.csv` | 10 |
| `sequence_data/PBMC_LCL_pilot_ill.csv` | `R3_HPRC_ill.csv` | 20 (Illumina TruPath R1 and R2) |
| `sample/PBMC_LCL_pilot_metadata.csv` | `R3_HPRC_metadata.csv` | 10 |
| `sample/PBMC_LCL_pilot_coverage_summary.csv` | `R3_HPRC_coverage_summary.csv` | 10 |

- Tissue (LCL or PBMC) is recorded in the existing R3 columns: `notes` (HiFi, Hi-C), `cell_type`
  (Kinnex) and `other_comments` (Illumina). All ONT data is LCL. The coverage summary `notes` give
  the HiFi LCL/PBMC split.
- `path` points to the pilot submission folders on S3 (`s3://human-pangenomics/submissions/...`).
- `coverage` = total bases / 3.3 Gb. For paired FASTQs (Omni-C, TruPath) each row holds half of the
  read pair's bases. ONT statistics are for pass reads.
- `ntsm_score` is the largest ntsm v1.2.1 score between the file and the other files of the same
  sample in the pilot all-vs-all evaluation; all are below 0.25 (same individual).
- Per-sample read N50s in the coverage summary are base-weighted means of the per-file N50s.
