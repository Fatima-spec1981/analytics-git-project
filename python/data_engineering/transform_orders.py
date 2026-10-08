import pandas as pd
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = PROJECT_ROOT / "data" / "raw" / "orders.csv"
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "orders.csv"

# Create processed directory
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
    "order_id",
    "customer_id",
    "order_status",
    "sales_channel",
    "payment_method"
]

for column in text_columns:
    df[column] = df[column].astype("string").str.strip()

# Convert order_date to datetime
df["order_date"] = pd.to_datetime(
    df["order_date"],
    errors="coerce"
)

# Convert order_total to numeric
df["order_total"] = pd.to_numeric(
    df["order_total"],
    errors="coerce"
)

# Remove exact duplicate records
df = df.drop_duplicates()

# Save processed data
df.to_csv(
    OUTPUT_FILE,
    index=False,
    date_format="%Y-%m-%d %H:%M:%S"
)

print("=== Order Transformation Complete ===")
print(f"Rows written: {len(df):,}")
print(f"Output file: {OUTPUT_FILE}")
print(f"order_date type: {df['order_date'].dtype}")
print(f"order_total type: {df['order_total'].dtype}")