select
    CUSTOMER_ID,
    FIRST_NAME,
    LAST_NAME,
    COUNTRY,
    CITY,
    SIGNUP_DATE,
    CUSTOMER_SEGMENT
from {{ source('ecommerce_snowflake', 'CUSTOMERS_RAW') }}
