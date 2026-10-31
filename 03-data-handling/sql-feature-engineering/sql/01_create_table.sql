DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    city TEXT,
    income INTEGER,
    purchase_amount INTEGER,
    purchase_date DATE
);