import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
INPUT_FILE = PROJECT_ROOT / "data" / "raw" / "order_items.csv"

df = pd.read_csv(INPUT_FILE)

print("=== Order Items Data Quality Report ===")

print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")

duplicate_count = df["order_item_id"].duplicated().sum()
print(f"Duplicate order_item_id: {duplicate_count}")

print("\nNull values:")
print(df.isnull().sum())

invalid_order_count = (~df["order_id"].isin(
    pd.read_csv(PROJECT_ROOT / "data" / "raw" / "orders.csv")["order_id"]
)).sum()

print(f"\nInvalid order_id references: {invalid_order_count}")

invalid_product_count = (~df["product_id"].isin(
    pd.read_csv(PROJECT_ROOT / "data" / "raw" / "products.csv")["product_id"]
)).sum()

print(f"Invalid product_id references: {invalid_product_count}")

negative_quantity_count = (df["quantity"] <= 0).sum()
print(f"Invalid quantity values: {negative_quantity_count}")

negative_price_count = (df["unit_price"] < 0).sum()
print(f"Negative unit_price values: {negative_price_count}")

if (
    duplicate_count == 0
    and df.isnull().sum().sum() == 0
    and invalid_order_count == 0
    and invalid_product_count == 0
    and negative_quantity_count == 0
    and negative_price_count == 0
):
    print("\nRESULT: PASS")
else:
    print("\nRESULT: REVIEW REQUIRED")