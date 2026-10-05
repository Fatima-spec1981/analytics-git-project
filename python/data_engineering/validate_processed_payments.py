import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
INPUT_FILE = PROJECT_ROOT / "data" / "processed" / "payments.csv"

df = pd.read_csv(
    INPUT_FILE,
    parse_dates=["payment_date"]
)

print("=== Processed Payments Data Quality Report ===")

print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")

duplicate_count = df["payment_id"].duplicated().sum()
print(f"Duplicate payment_id: {duplicate_count}")

print("\nNull values:")
print(df.isnull().sum())

invalid_date_count = df["payment_date"].isna().sum()
print(f"\nInvalid payment_date values: {invalid_date_count}")

negative_amount_count = (df["payment_amount"] < 0).sum()
print(f"Negative payment_amount values: {negative_amount_count}")

expected_columns = [
    "payment_id",
    "order_id",
    "payment_date",
    "payment_method",
    "payment_status",
    "payment_amount"
]

columns_match = list(df.columns) == expected_columns
print(f"Columns match expected structure: {columns_match}")

if (
    duplicate_count == 0
    and df.isnull().sum().sum() == 0
    and invalid_date_count == 0
    and negative_amount_count == 0
    and columns_match
):
    print("\nRESULT: PASS")
else:
    print("\nRESULT: REVIEW REQUIRED")