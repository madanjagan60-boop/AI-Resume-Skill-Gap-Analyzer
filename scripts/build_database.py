import pandas as pd
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = BASE_DIR / "data" / "raw"
OUTPUT_FILE = BASE_DIR / "data" / "processed" / "technical_skills_database.csv"

# Read all CSV files
csv_files = list(RAW_DATA_PATH.glob("*.csv"))

all_data = []

for file in csv_files:
    print(f"Reading: {file.name}")

    df = pd.read_csv(file)

    all_data.append(df)

# Merge all data
master_df = pd.concat(all_data, ignore_index=True)

# Remove duplicate skills
master_df = master_df.drop_duplicates(subset=["Skill"])

# Sort alphabetically
master_df = master_df.sort_values(by="Skill")

# Save processed database
master_df.to_csv(OUTPUT_FILE, index=False)

print("\nDatabase created successfully!")
print(f"Total Skills: {len(master_df)}")
print(f"Saved to: {OUTPUT_FILE}")