"""
detect_transits.py
------------------
Runs the Box Least Squares (BLS) algorithm to detect potential transits
and saves key parameters to data/processed/bls_results.csv.
"""

import pandas as pd
import numpy as np
from astropy.timeseries import BoxLeastSquares
from pathlib import Path

def detect_transits(target_id: str, input_dir: str = "../data/processed", output_dir: str = "../data/processed"):
    df = pd.read_csv(Path(input_dir) / f"{target_id}_detrended.csv")
    t, f = df["time"].to_numpy(), df["flux"].to_numpy()

    bls = BoxLeastSquares(t, f)
    periods = np.linspace(0.5, 10, 2000)
    durations = np.linspace(0.05, 0.25, 20)
    result = bls.power(periods, durations)

    best = np.argmax(result.power)
    out = {
        "target": target_id,
        "period_days": result.period[best],
        "t0_bkjd": result.transit_time[best],
        "duration_days": result.duration[best],
        "depth_ppm": result.depth[best] * 1e6,
        "snr": result.power[best]
    }

    pd.DataFrame([out]).to_csv(Path(output_dir) / f"{target_id}_bls_results.csv", index=False)
    print(f"[✓] Saved BLS results: {output_dir}/{target_id}_bls_results.csv")

if __name__ == "__main__":
    detect_transits("Kepler-10")
