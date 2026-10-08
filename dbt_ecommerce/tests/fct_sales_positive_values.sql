select
    order_item_id,
    quantity,
    unit_price
from {{ ref('fct_sales') }}
where quantity <= 0
   or unit_price < 0