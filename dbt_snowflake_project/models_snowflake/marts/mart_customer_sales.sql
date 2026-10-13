select
    CUSTOMER_ID,
    FIRST_NAME,
    LAST_NAME,
    COUNTRY,
    CUSTOMER_SEGMENT,
    count(distinct ORDER_ID) as TOTAL_ORDERS,
    sum(ORDER_TOTAL) as TOTAL_SPENT
from {{ ref('int_orders_customers') }}
group by
    CUSTOMER_ID,
    FIRST_NAME,
    LAST_NAME,
    COUNTRY,
    CUSTOMER_SEGMENT
