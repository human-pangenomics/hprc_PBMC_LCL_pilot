# Pilot sequence data tables

Per-file tables for the PBMC + LCL pilot, one per technology, using the same columns as the
[R3_HPRC `sequence_data` tables](https://github.com/human-pangenomics/R3_HPRC/tree/main/sequence_data).

| Table | R3 equivalent | Files | Contents |
|---|---|---|---|
| `PBMC_LCL_pilot_hifi.csv` | `R3_HPRC_hifi_no_dc_map.csv` | 36 | PacBio HiFi BAMs: 18 LCL (Fiber-seq) + 18 PBMC. The `notes` column says which |
| `PBMC_LCL_pilot_ont.csv` | `R3_HPRC_ont.csv` | 22 | ONT ultra-long BAMs (LCL) |
| `PBMC_LCL_pilot_hic.csv` | `R3_HPRC_hic.csv` | 80 | Omni-C FASTQs (LCL), R1 and R2 rows |
| `PBMC_LCL_pilot_kinnex.csv` | `R3_HPRC_kinnex.csv` | 10 | Kinnex IsoSeq FLNC BAMs (LCL) |
| `PBMC_LCL_pilot_ill.csv` | `R3_HPRC_ill.csv` | 20 | Illumina TruPath FASTQs (LCL), R1 and R2 rows |

Conventions:

- `path` points to the pilot submission folders on S3 (`s3://human-pangenomics/submissions/...`),
  the same locations linked from the data panel in the top-level README.
- `coverage` = total bases / 3.3 Gb. For paired FASTQs (Omni-C, TruPath) each row holds half of
  the read pair's bases.
- ONT statistics are for pass reads only.
- `ntsm_score` is the largest ntsm v1.2.1 score between that file and every other file from the
  same sample in the pilot all-vs-all evaluation (HiFi, ONT, Omni-C and Kinnex). Scores below
  ~0.25 indicate the same individual. Omni-C R2 rows carry the score of their R1 file. TruPath
  has no `ntsm_score` column in the R3 Illumina format.
- Accessions, BioSamples and fields not recorded in the deliveries are left blank.

Per-sample tables in `../sample/` follow the R3_HPRC `sample/` tables: `PBMC_LCL_pilot_metadata.csv`
(sex; population not recorded) and `PBMC_LCL_pilot_coverage_summary.csv` (coverage per technology,
summed from the tables above; HiFi and ONT read N50s are base-weighted means of the per-file N50s).
