import pandas as pd
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]

ORDERS_FILE = PROJECT_ROOT / "data" / "raw" / "orders.csv"
CUSTOMERS_FILE = PROJECT_ROOT / "data" / "raw" / "customers.csv"

# Load data
orders = pd.read_csv(ORDERS_FILE)
customers = pd.read_csv(CUSTOMERS_FILE)

print("=== Orders Data Quality Report ===")

# Basic information
print(f"Rows: {len(orders):,}")
print(f"Columns: {len(orders.columns)}")

# Duplicate order_id
duplicate_order_count = orders["order_id"].duplicated().sum()
print(f"Duplicate order_id: {duplicate_order_count}")

# Null check
print("\nNull values:")
print(orders.isnull().sum())

# Customer relationship validation
invalid_customer_count = (
    ~orders["customer_id"].isin(customers["customer_id"])
).sum()

print(
    f"\nOrders with invalid customer_id: "
    f"{invalid_customer_count}"
)

# Valid order statuses
valid_order_statuses = [
    "Completed",
    "Processing",
    "Shipped",
    "Cancelled",
    "Returned"
]

invalid_order_status_count = (
    ~orders["order_status"].isin(valid_order_statuses)
).sum()

print(
    f"Invalid order_status values: "
    f"{invalid_order_status_count}"
)

# Valid sales channels
valid_sales_channels = [
    "Web",
    "Mobile App",
    "Marketplace"
]

invalid_sales_channel_count = (
    ~orders["sales_channel"].isin(valid_sales_channels)
).sum()

print(
    f"Invalid sales_channel values: "
    f"{invalid_sales_channel_count}"
)

# Valid payment methods
valid_payment_methods = [
    "Card",
    "PayPal",
    "Apple Pay",
    "Google Pay",
    "Bank Transfer"
]

invalid_payment_method_count = (
    ~orders["payment_method"].isin(valid_payment_methods)
).sum()

print(
    f"Invalid payment_method values: "
    f"{invalid_payment_method_count}"
)

# Order total validation
negative_order_total_count = (
    orders["order_total"] < 0
).sum()

print(
    f"Negative order_total values: "
    f"{negative_order_total_count}"
)

# Final result
if (
    duplicate_order_count == 0
    and orders.isnull().sum().sum() == 0
    and invalid_customer_count == 0
    and invalid_order_status_count == 0
    and invalid_sales_channel_count == 0
    and invalid_payment_method_count == 0
    and negative_order_total_count == 0
):
    print("\nRESULT: PASS")
else:
    print("\nRESULT: REVIEW REQUIRED")