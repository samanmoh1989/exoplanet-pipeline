"""
download_data.py
----------------
Downloads light curve data for a given Kepler or TESS target ID
and saves it as a CSV in data/raw/.
"""

from lightkurve import search_lightcurve
import pandas as pd
from pathlib import Path

def download_lightcurve(target_id: str, mission: str = "Kepler", output_dir: str = "../data/raw"):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    lc = search_lightcurve(target_id, mission=mission).download()
    df = lc.to_pandas()
    df.to_csv(output_dir / f"{target_id}_raw.csv", index=False)
    print(f"[✓] Saved raw lightcurve: {output_dir}/{target_id}_raw.csv")

if __name__ == "__main__":
    # Example:
    download_lightcurve("Kepler-10")
