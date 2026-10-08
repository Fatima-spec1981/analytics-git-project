import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = PROJECT_ROOT / "data" / "raw" / "payments.csv"
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "payments.csv"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT_FILE)

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

text_columns = [
    "payment_id",
    "order_id",
    "payment_method",
    "payment_status"
]

for column in text_columns:
    df[column] = df[column].astype("string").str.strip()

df["payment_date"] = pd.to_datetime(
    df["payment_date"],
    errors="coerce"
)

df["payment_amount"] = pd.to_numeric(
    df["payment_amount"],
    errors="coerce"
)

df = df.drop_duplicates()

df.to_csv(
    OUTPUT_FILE,
    index=False,
    date_format="%Y-%m-%d %H:%M:%S"
)

print("=== Payment Transformation Complete ===")
print(f"Rows written: {len(df):,}")
print(f"Output file: {OUTPUT_FILE}")
print(f"payment_date type: {df['payment_date'].dtype}")
print(f"payment_amount type: {df['payment_amount'].dtype}")