SELECT city, SUM(purchase_amount) AS total_revenue
FROM customers GROUP BY city ORDER BY total_revenue DESC;

SELECT income_bracket, AVG(purchase_amount)
FROM customers GROUP BY income_bracket;

SELECT name, purchase_amount
FROM customers ORDER BY purchase_amount DESC LIMIT 3;

SELECT name, purchase_amount,
RANK() OVER (ORDER BY purchase_amount DESC) AS spend_rank
FROM customers;

SELECT purchase_month, SUM(purchase_amount) AS monthly_revenue
FROM customers GROUP BY purchase_month ORDER BY purchase_month;