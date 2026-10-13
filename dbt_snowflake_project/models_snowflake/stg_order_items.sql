select
    ORDER_ITEM_ID as ITEM_ID,
    ORDER_ID,
    PRODUCT_ID,
    QUANTITY,
    UNIT_PRICE,
    DISCOUNT_PCT,
    LINE_AMOUNT
from {{ source('ecommerce_snowflake', 'ORDER_ITEMS_RAW') }}
