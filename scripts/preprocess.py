"""
preprocess.py
-------------
Cleans and detrends the light curve using Lightkurve.
Saves detrended curve to data/processed/.
"""

import pandas as pd
from lightkurve import LightCurve
from pathlib import Path

def preprocess_lightcurve(target_id: str, input_dir: str = "../data/raw", output_dir: str = "../data/processed"):
    input_path = Path(input_dir) / f"{target_id}_raw.csv"
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(input_path)
    lc = LightCurve(time=df["time"], flux=df["flux"])
    detrended = lc.remove_outliers(sigma=5).flatten(window_length=401)
    detrended.to_pandas().to_csv(output_dir / f"{target_id}_detrended.csv", index=False)
    print(f"[✓] Saved detrended lightcurve: {output_dir}/{target_id}_detrended.csv")

if __name__ == "__main__":
    preprocess_lightcurve("Kepler-10")
