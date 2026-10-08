select
    order_item_id,
    discount_pct
from {{ ref('fct_sales') }}
where discount_pct < 0
   or discount_pct > 1