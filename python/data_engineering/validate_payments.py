import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
INPUT_FILE = PROJECT_ROOT / "data" / "raw" / "payments.csv"

df = pd.read_csv(INPUT_FILE)

print("=== Payments Data Quality Report ===")

print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")

duplicate_count = df["payment_id"].duplicated().sum()
print(f"Duplicate payment_id: {duplicate_count}")

print("\nNull values:")
print(df.isnull().sum())

orders = pd.read_csv(
    PROJECT_ROOT / "data" / "raw" / "orders.csv"
)

invalid_order_count = (
    ~df["order_id"].isin(orders["order_id"])
).sum()

print(f"\nInvalid order_id references: {invalid_order_count}")

negative_amount_count = (df["payment_amount"] < 0).sum()
print(f"Negative payment_amount values: {negative_amount_count}")

if (
    duplicate_count == 0
    and df.isnull().sum().sum() == 0
    and invalid_order_count == 0
    and negative_amount_count == 0
):
    print("\nRESULT: PASS")
else:
    print("\nRESULT: REVIEW REQUIRED")