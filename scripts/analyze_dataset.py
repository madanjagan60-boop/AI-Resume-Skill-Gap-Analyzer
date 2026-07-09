from pathlib import Path
import pandas as pd

RAW_DATA = Path("data/raw")

total_rows = 0

print("=" * 60)
print("DATASET ANALYSIS")
print("=" * 60)

for file in sorted(RAW_DATA.glob("*.csv")):
    df = pd.read_csv(file)

    rows = len(df)
    total_rows += rows

    print(f"{file.name:<30} {rows:>5} skills")

print("-" * 60)
print(f"TOTAL ROWS: {total_rows}")
print("=" * 60)