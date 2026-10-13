select
    ORDER_DATE,
    count(distinct ORDER_ID) as TOTAL_ORDERS,
    sum(ORDER_TOTAL) as TOTAL_REVENUE
from {{ ref('stg_orders') }}
group by ORDER_DATE
