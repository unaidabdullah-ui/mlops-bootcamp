CREATE VIEW clean_customer_data AS
SELECT id, name, age, city, income, purchase_amount,
       purchase_month, high_value_customer, income_bracket
FROM customers;