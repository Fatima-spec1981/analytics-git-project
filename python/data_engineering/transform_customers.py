import pandas as pd
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = PROJECT_ROOT / "data" / "raw" / "customers.csv"
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "customers.csv"

# Create processed directory if it doesn't exist
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load raw data
df = pd.read_csv(INPUT_FILE)

# Standardize column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Clean text fields
text_columns = [
    "first_name",
    "last_name",
    "country",
    "city",
    "customer_segment"
]

for column in text_columns:
    df[column] = df[column].astype("string").str.strip()

# Convert signup_date to proper date type
df["signup_date"] = pd.to_datetime(
    df["signup_date"],
    errors="coerce"
)

# Remove exact duplicate records
df = df.drop_duplicates()

# Save processed data
df.to_csv(
    OUTPUT_FILE,
    index=False,
    date_format="%Y-%m-%d"
)

print("=== Customer Transformation Complete ===")
print(f"Rows written: {len(df):,}")
print(f"Output file: {OUTPUT_FILE}")
print(f"signup_date type: {df['signup_date'].dtype}")