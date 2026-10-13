select
    ORDER_ID,
    CUSTOMER_ID,
    ORDER_DATE,
    ORDER_STATUS as STATUS,
    SALES_CHANNEL as CHANNEL,
    PAYMENT_METHOD,
    ORDER_TOTAL
from {{ source('ecommerce_snowflake', 'ORDERS_RAW') }}
