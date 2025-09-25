-- Create orders table
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(50),
    product VARCHAR(50),
    quantity INT,
    price NUMERIC(10,2),
    order_date DATE
);

-- Insert sample data
INSERT INTO orders (customer_name, product, quantity, price, order_date) VALUES
('Omar', 'Laptop', 1, 1500.00, '2025-09-01'),
('Ali', 'Phone', 2, 600.00, '2025-09-01'),
('Sara', 'Tablet', 1, 300.00, '2025-09-02'),
('Mona', 'Laptop', 1, 1500.00, '2025-09-03'),
('John', 'Phone', 3, 600.00, '2025-09-03'),
('Omar', 'Headphones', 2, 120.00, '2025-09-04'),
('Ali', 'Laptop', 1, 1500.00, '2025-09-04'),
('Sara', 'Phone', 1, 600.00, '2025-09-05'),
('Mona', 'Tablet', 2, 300.00, '2025-09-05'),
('John', 'Laptop', 1, 1500.00, '2025-09-06'),
('Omar', 'Tablet', 1, 300.00, '2025-09-07'),
('Ali', 'Headphones', 3, 120.00, '2025-09-07'),
('Sara', 'Laptop', 1, 1500.00, '2025-09-08'),
('Mona', 'Phone', 2, 600.00, '2025-09-08'),
('John', 'Tablet', 1, 300.00, '2025-09-09'),
('Omar', 'Phone', 2, 600.00, '2025-09-10'),
('Ali', 'Tablet', 2, 300.00, '2025-09-11'),
('Sara', 'Headphones', 1, 120.00, '2025-09-11'),
('Mona', 'Laptop', 2, 1500.00, '2025-09-12'),
('John', 'Headphones', 4, 120.00, '2025-09-12');
