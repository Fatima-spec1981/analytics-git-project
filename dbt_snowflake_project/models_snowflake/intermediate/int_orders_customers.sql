select
    o.ORDER_ID,
    o.CUSTOMER_ID,
    o.ORDER_DATE,
    o.STATUS,
    o.CHANNEL,
    o.PAYMENT_METHOD,
    o.ORDER_TOTAL,
    c.FIRST_NAME,
    c.LAST_NAME,
    c.CITY,
    c.COUNTRY,
    c.CUSTOMER_SEGMENT
from {{ ref('stg_orders') }} as o
left join {{ ref('stg_customers') }} as c
    on o.CUSTOMER_ID = c.CUSTOMER_ID
