# 🪐 Exoplanet Discovery — Transit Detection Pipeline

This project demonstrates a **full data pipeline** for discovering potential **exoplanet transits** from Kepler/TESS light curves using Python and scientific tools like Lightkurve and Astropy.

---

## 🚀 Overview

### Pipeline Structure

1. **01_download_and_explore.ipynb**
   - Search and download target light curves (e.g., Kepler or TESS).
   - Inspect flux columns and data quality flags.
   - Save raw CSV to `data/raw/`.

2. **02_preprocess_and_bls.ipynb**
   - Clean and detrend the light curve.
   - Apply Box Least Squares (BLS) periodogram.
   - Find best-fit orbital period and phase-folded light curve.
   - Save processed data to `data/processed/`.

3. **03_feature_engineering_and_modeling.ipynb**
   - Load BLS results and create derived features (period, depth, SNR, duty cycle).
   - Compute a baseline candidate score or train ML model (if enough data).

4. **04_evaluate_results.ipynb**
   - Generate and save plots: periodogram and phase-folded light curves.
   - Export a `RESULTS.md` report under `reports/` for publication or GitHub.

---

## 📂 Directory Layout

```
project-root/
├── data/
│   ├── raw/                 # Unprocessed downloaded CSVs
│   ├── processed/           # Cleaned, detrended, and BLS outputs
│
├── notebooks/
│   ├── 01_download_and_explore.ipynb
│   ├── 02_preprocess_and_bls.ipynb
│   ├── 03_feature_engineering_and_modeling.ipynb
│   └── 04_evaluate_results.ipynb
│
├── reports/
│   ├── figures/             # Saved plots (periodogram, folded light curves)
│   └── RESULTS.md           # Markdown summary of best candidate
│
├── scripts/
│   └── (optional automation scripts)
│
└── README.md
```

---

## 🧠 Requirements

Install all dependencies using `pip`:

```bash
pip install -r requirements.txt
```

or manually:

```bash
pip install lightkurve astropy pandas numpy matplotlib scipy scikit-learn
```

---

## ⚙️ Example Command Flow

You can reproduce the analysis in order:

```bash
jupyter notebook notebooks/01_download_and_explore.ipynb
jupyter notebook notebooks/02_preprocess_and_bls.ipynb
jupyter notebook notebooks/03_feature_engineering_and_modeling.ipynb
jupyter notebook notebooks/04_evaluate_results.ipynb
```

---

## 🪄 Output Artifacts

| Type | Path | Description |
|------|------|--------------|
| CSV  | `data/raw/sample.csv` | Original downloaded light curve |
| CSV  | `data/processed/detrended_lightcurve.csv` | Clean, detrended flux data |
| CSV  | `data/processed/bls_results.csv` | BLS-derived parameters |
| PNG  | `reports/figures/bls_periodogram.png` | BLS power vs. period plot |
| PNG  | `reports/figures/phase_folded_binned.png` | Folded transit light curve |
| MD   | `reports/RESULTS.md` | Markdown summary of findings |

---

## 📊 Future Work

- Integrate multiple targets into a labeled dataset.
- Train RandomForest / MLP models to classify candidates.
- Cross-match with Gaia DR3 for stellar parameters.
- Extend to full TESS sectors.

---

## 🧾 Citation

If you use this repository in your research, please cite:

```
Author: Saman (ScienceMood)
Project: Exoplanet Discovery — Transit Detection Pipeline
URL: https://sciencemood.com/
```

---
Exoplanet Candidate — Results
This report summarizes the outcome of our transit search.

Key Parameters
Best period: 0.837538 days
Transit duration: 1.68 hours
Transit depth: ~165.0 ppm
SNR: 2.55
Figures
BLS Periodogram: reports/figures/bls_periodogram.png
Phase-folded (raw): reports/figures/phase_folded_raw.png
Phase-folded (binned): reports/figures/phase_folded_binned.png
Notes
Period aliases and harmonics should be checked (P/2, 2P).
The candidate appears to show a repeatable, U-shaped dip near phase 0.
Future work: vetting tests, stellar parameter cross-match, and ML-based ranking on a larger sample.

## 🪐 License

This project is released under the **MIT License** — free to use, modify, and distribute.


