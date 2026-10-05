import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
INPUT_FILE = PROJECT_ROOT / "data" / "processed" / "order_items.csv"

df = pd.read_csv(INPUT_FILE)

print("=== Processed Order Items Data Quality Report ===")

print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")

duplicate_count = df["order_item_id"].duplicated().sum()
print(f"Duplicate order_item_id: {duplicate_count}")

print("\nNull values:")
print(df.isnull().sum())

orders = pd.read_csv(
    PROJECT_ROOT / "data" / "processed" / "orders.csv"
)

products = pd.read_csv(
    PROJECT_ROOT / "data" / "processed" / "products.csv"
)

invalid_order_count = (
    ~df["order_id"].isin(orders["order_id"])
).sum()

print(f"\nInvalid order_id references: {invalid_order_count}")

invalid_product_count = (
    ~df["product_id"].isin(products["product_id"])
).sum()

print(f"Invalid product_id references: {invalid_product_count}")

invalid_quantity_count = (df["quantity"] <= 0).sum()
print(f"Invalid quantity values: {invalid_quantity_count}")

negative_price_count = (df["unit_price"] < 0).sum()
print(f"Negative unit_price values: {negative_price_count}")

negative_discount_count = (df["discount_pct"] < 0).sum()
print(f"Negative discount_pct values: {negative_discount_count}")

negative_amount_count = (df["line_amount"] < 0).sum()
print(f"Negative line_amount values: {negative_amount_count}")

expected_columns = [
    "order_item_id",
    "order_id",
    "product_id",
    "quantity",
    "unit_price",
    "discount_pct",
    "line_amount"
]

columns_match = list(df.columns) == expected_columns
print(f"Columns match expected structure: {columns_match}")

if (
    duplicate_count == 0
    and df.isnull().sum().sum() == 0
    and invalid_order_count == 0
    and invalid_product_count == 0
    and invalid_quantity_count == 0
    and negative_price_count == 0
    and negative_discount_count == 0
    and negative_amount_count == 0
    and columns_match
):
    print("\nRESULT: PASS")
else:
    print("\nRESULT: REVIEW REQUIRED")