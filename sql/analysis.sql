
-- Top Products by Profit
SELECT product_name, SUM(profit) AS total_profit
FROM superstore
GROUP BY product_name
ORDER BY total_profit DESC
LIMIT 10;

-- Monthly Sales Trend
SELECT year, SUM(sales) AS total_sales
FROM superstore
GROUP BY year
ORDER BY year;
