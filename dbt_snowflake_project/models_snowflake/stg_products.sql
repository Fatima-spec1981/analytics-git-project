select
    PRODUCT_ID,
    PRODUCT_NAME,
    CATEGORY,
    BRAND,
    UNIT_COST,
    UNIT_PRICE,
    STOCK_STATUS
from {{ source('ecommerce_snowflake', 'PRODUCTS_RAW') }}
