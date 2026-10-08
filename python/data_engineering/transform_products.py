import pandas as pd
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = PROJECT_ROOT / "data" / "raw" / "products.csv"
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "products.csv"

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
    "product_id",
    "product_name",
    "category",
    "brand",
    "stock_status"
]

for column in text_columns:
    df[column] = df[column].astype("string").str.strip()

# Convert numeric fields
df["unit_cost"] = pd.to_numeric(df["unit_cost"], errors="coerce")
df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")

# Remove exact duplicate records
df = df.drop_duplicates()

# Save processed data
df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("=== Product Transformation Complete ===")
print(f"Rows written: {len(df):,}")
print(f"Output file: {OUTPUT_FILE}")
print(f"unit_cost type: {df['unit_cost'].dtype}")
print(f"unit_price type: {df['unit_price'].dtype}")