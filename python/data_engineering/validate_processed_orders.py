import pandas as pd
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]
INPUT_FILE = PROJECT_ROOT / "data" / "processed" / "orders.csv"

# Load processed data
df = pd.read_csv(
    INPUT_FILE,
    parse_dates=["order_date"]
)

print("=== Processed Orders Data Quality Report ===")

# Basic information
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")

# Duplicate check
duplicate_count = df["order_id"].duplicated().sum()
print(f"Duplicate order_id: {duplicate_count}")

# Null check
print("\nNull values:")
print(df.isnull().sum())

# Date validation
invalid_date_count = df["order_date"].isna().sum()
print(f"\nInvalid order_date values: {invalid_date_count}")

# Order total validation
negative_total_count = (df["order_total"] < 0).sum()
print(f"Negative order_total values: {negative_total_count}")

# Expected columns
expected_columns = [
    "order_id",
    "customer_id",
    "order_date",
    "order_status",
    "sales_channel",
    "payment_method",
    "order_total"
]

columns_match = list(df.columns) == expected_columns
print(f"Columns match expected structure: {columns_match}")

# Final validation
if (
    duplicate_count == 0
    and df.isnull().sum().sum() == 0
    and invalid_date_count == 0
    and negative_total_count == 0
    and columns_match
):
    print("\nRESULT: PASS")
else:
    print("\nRESULT: REVIEW REQUIRED")