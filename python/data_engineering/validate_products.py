import pandas as pd
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]
INPUT_FILE = PROJECT_ROOT / "data" / "raw" / "products.csv"

# Load raw data
df = pd.read_csv(INPUT_FILE)

print("=== Products Data Quality Report ===")

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

print(
    f"Invalid stock_status values: "
    f"{invalid_stock_status_count}"
)

# Final result
if (
    duplicate_count == 0
    and df.isnull().sum().sum() == 0
    and invalid_price_count == 0
    and invalid_stock_status_count == 0
):
    print("\nRESULT: PASS")
else:
    print("\nRESULT: REVIEW REQUIRED")