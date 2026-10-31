ALTER TABLE customers ADD COLUMN purchase_month INTEGER;
UPDATE customers SET purchase_month = strftime('%m', purchase_date);

ALTER TABLE customers ADD COLUMN high_value_customer TEXT;
UPDATE customers
SET high_value_customer = CASE WHEN purchase_amount >= 3000 THEN 'Yes' ELSE 'No' END;

ALTER TABLE customers ADD COLUMN income_bracket TEXT;
UPDATE customers
SET income_bracket = 
    CASE 
        WHEN income < 50000 THEN 'Low'
        WHEN income BETWEEN 50000 AND 70000 THEN 'Medium'
        ELSE 'High'
    END;