with products as (

    select *
    from {{ source('ecommerce', 'products') }}

),

final as (

    select
        product_id,
        product_name,
        category,
        subcategory,
        unit_cost,
        unit_price,
        stock_status
    from products

)

select *
from final