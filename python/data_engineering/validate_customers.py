import pandas as pd
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]
INPUT_FILE = PROJECT_ROOT / "data" / "raw" / "customers.csv"

# Load data
df = pd.read_csv(INPUT_FILE)

print("=== Customers Data Quality Report ===")
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

# Final result
if duplicate_count == 0 and df.isnull().sum().sum() == 0:
    print("\nRESULT: PASS")
else:
    print("\nRESULT: REVIEW REQUIRED")