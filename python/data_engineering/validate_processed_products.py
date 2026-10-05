import pandas as pd
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]
INPUT_FILE = PROJECT_ROOT / "data" / "processed" / "products.csv"

# Load processed data
df = pd.read_csv(INPUT_FILE)

print("=== Processed Products Data Quality Report ===")

# Basic information
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")

# Duplicate check
duplicate_count = df["product_id"].duplicated().sum()
print(f"Duplicate product_id: {duplicate_count}")

# Null check
print("\nNull values:")
print(df.isnull().sum())

# Price validation
invalid_price_count = (df["unit_price"] < df["unit_cost"]).sum()
print(f"\nProducts where unit_price < unit_cost: {invalid_price_count}")

# Stock status validation
valid_stock_statuses = [
    "In Stock",
    "Low Stock",
    "Out of Stock",
    "Discontinued"
]

invalid_stock_status_count = (
    ~df["stock_status"].isin(valid_stock_statuses)
).sum()

print(f"Invalid stock_status values: {invalid_stock_status_count}")

# Expected columns
expected_columns = [
    "product_id",
    "product_name",
    "category",
    "brand",
    "unit_cost",
    "unit_price",
    "stock_status"
]

columns_match = list(df.columns) == expected_columns
print(f"Columns match expected structure: {columns_match}")

# Final validation
if (
    duplicate_count == 0
    and df.isnull().sum().sum() == 0
    and invalid_price_count == 0
    and invalid_stock_status_count == 0
    and columns_match
):
    print("\nRESULT: PASS")
else:
    print("\nRESULT: REVIEW REQUIRED")