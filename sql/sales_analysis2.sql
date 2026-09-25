-- Sales analysis by product category
-- Calculates total sales for each product category.

SELECT
    product_category,
    SUM(sales_amount) AS total_sales
FROM sales
GROUP BY product_category
ORDER BY total_sales DESC;