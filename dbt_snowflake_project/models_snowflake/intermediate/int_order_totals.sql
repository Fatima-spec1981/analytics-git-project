select
    ORDER_ID,
    sum(LINE_AMOUNT) as ITEMS_TOTAL,
    sum(QUANTITY) as TOTAL_ITEMS
from {{ ref('stg_order_items') }}
group by ORDER_ID
