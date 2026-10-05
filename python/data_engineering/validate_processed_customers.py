import pandas as pd
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]
INPUT_FILE = PROJECT_ROOT / "data" / "processed" / "customers.csv"

# Load processed data
df = pd.read_csv(INPUT_FILE, parse_dates=["signup_date"])

print("=== Processed Customers Data Quality Report ===")

# Basic information
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")

# Duplicate check
duplicate_count = df["customer_id"].duplicated().sum()
print(f"Duplicate customer_id: {duplicate_count}")

# Null check
print("\nNull values:")
print(df.isnull().sum())

# Data types
print("\nData types:")
print(df.dtypes)

# Expected columns
expected_columns = [
    "customer_id",
    "first_name",
    "last_name",
    "country",
    "city",
    "signup_date",
    "customer_segment"
]

columns_match = list(df.columns) == expected_columns
print(f"\nColumns match expected structure: {columns_match}")

# Final validation
if (
    duplicate_count == 0
    and df.isnull().sum().sum() == 0
    and columns_match
    and pd.api.types.is_datetime64_any_dtype(df["signup_date"])
):
    print("\nRESULT: PASS")
else:
    print("\nRESULT: REVIEW REQUIRED")