DELETE FROM customers
WHERE name IS NULL OR purchase_date IS NULL;

UPDATE customers SET income = 0 WHERE income IS NULL;
UPDATE customers SET purchase_amount = 0 WHERE purchase_amount IS NULL;
UPDATE customers SET city = 'Unknown' WHERE city IS NULL;

UPDATE customers
SET age = (SELECT AVG(age) FROM customers)
WHERE age IS NULL;