with sales as (

    select *
    from {{ ref('int_order_items') }}

),

final as (

    select
        order_item_id,
        order_id,
        customer_id,
        product_id,
        order_date,
        order_status,
        sales_channel,
        payment_method,
        quantity,
        unit_price,
        discount_pct,
        line_amount,

        cast(quantity * unit_price as decimal(18,2)) as gross_sales,

        cast(
            (quantity * unit_price) * discount_pct
            as decimal(18,2)
        ) as discount_amount,

        cast(line_amount as decimal(18,2)) as net_sales

    from sales

)

select *
from final