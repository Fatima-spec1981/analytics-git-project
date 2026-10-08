with source as (

    select *
    from {{ source('ecommerce', 'orders') }}

),

renamed as (

    select
        order_id,
        customer_id,
        order_date,
        order_status,
        sales_channel,
        payment_method,
        order_total
    from source

)

select *
from renamed