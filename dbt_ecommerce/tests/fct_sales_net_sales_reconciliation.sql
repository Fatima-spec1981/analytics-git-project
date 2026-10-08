select
    order_item_id,
    gross_sales,
    discount_amount,
    net_sales,
    ABS(
        (gross_sales - discount_amount) - net_sales
    ) as difference

from {{ ref('fct_sales') }}

where ABS(
    (gross_sales - discount_amount) - net_sales
) > 0.01