-- Sales analysis by product category

SELECT
    product_category,
    SUM(sales_amount) AS total_sales
FROM sales
GROUP BY product_category
ORDER BY total_sales DESC;