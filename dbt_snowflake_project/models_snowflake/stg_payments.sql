select
    PAYMENT_ID,
    ORDER_ID,
    PAYMENT_DATE,
    PAYMENT_METHOD,
    PAYMENT_STATUS,
    PAYMENT_AMOUNT
from {{ source('ecommerce_snowflake', 'PAYMENTS_RAW') }}
