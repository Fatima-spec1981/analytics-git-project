with customers as (

    select *
    from {{ source('ecommerce', 'customers') }}

),

final as (

    select
        customer_id,
        first_name,
        last_name,
        email,
        country,
        city,
        signup_date
    from customers

)

select *
from final