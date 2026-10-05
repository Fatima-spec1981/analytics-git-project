import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = PROJECT_ROOT / "data" / "raw" / "order_items.csv"
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "order_items.csv"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT_FILE)

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

text_columns = [
    "order_item_id",
    "order_id",
    "product_id"
]

for column in text_columns:
    df[column] = df[column].astype("string").str.strip()

numeric_columns = [
    "quantity",
    "unit_price",
    "discount_pct",
    "line_amount"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )

df = df.drop_duplicates()

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("=== Order Items Transformation Complete ===")
print(f"Rows written: {len(df):,}")
print(f"Output file: {OUTPUT_FILE}")
print(f"quantity type: {df['quantity'].dtype}")
print(f"unit_price type: {df['unit_price'].dtype}")
print(f"discount_pct type: {df['discount_pct'].dtype}")
print(f"line_amount type: {df['line_amount'].dtype}")