with order_items as (

    select *
    from {{ ref('stg_order_items') }}

),

orders as (

    select *
    from {{ ref('stg_orders') }}

),

joined as (

    select
        oi.order_item_id,
        oi.order_id,
        oi.product_id,
        oi.quantity,
        oi.unit_price,
        oi.discount_pct,
        oi.line_amount,
        o.customer_id,
        o.order_date,
        o.order_status,
        o.sales_channel,
        o.payment_method,
        o.order_total
    from order_items oi
    left join orders o
        on oi.order_id = o.order_id

)

select *
from joined