-- ======================
-- Customer Table
-- ======================
CREATE TABLE Customer (
    cust_id      INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name         VARCHAR(100) NOT NULL,
    email        VARCHAR(150) UNIQUE NOT NULL,
    phone        VARCHAR(20),
    address      VARCHAR(255),
    created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ======================
-- Product Table
-- ======================
CREATE TABLE Product (
    prod_id      INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name         VARCHAR(100) NOT NULL,
    description  VARCHAR(255),
    price        DECIMAL(10,2) NOT NULL,
    stock_qty    INTEGER DEFAULT 0,
    created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ======================
-- Order Table
-- ======================
CREATE TABLE Orders (
    order_id     INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    cust_id      INTEGER NOT NULL,
    order_date   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status       VARCHAR(20) DEFAULT 'Pending',
    total_amount DECIMAL(12,2) DEFAULT 0,

    CONSTRAINT fk_orders_customer
        FOREIGN KEY (cust_id) REFERENCES Customer(cust_id)
);

-- ======================
-- OrderItem Table (junction table for M:N)
-- ======================
CREATE TABLE OrderItem (
    order_id     INTEGER NOT NULL,
    prod_id      INTEGER NOT NULL,
    quantity     INTEGER NOT NULL,
    price        DECIMAL(10,2) NOT NULL,

    PRIMARY KEY (order_id, prod_id),

    CONSTRAINT fk_orderitem_order
        FOREIGN KEY (order_id) REFERENCES Orders(order_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_orderitem_product
        FOREIGN KEY (prod_id) REFERENCES Product(prod_id)
);

-- ======================
-- Payment Table
-- ======================
CREATE TABLE Payment (
    pay_id       INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    order_id     INTEGER UNIQUE NOT NULL,
    amount       DECIMAL(12,2) NOT NULL,
    method       VARCHAR(30) NOT NULL,
    status       VARCHAR(20) DEFAULT 'Pending',
    paid_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_payment_order
        FOREIGN KEY (order_id) REFERENCES Orders(order_id)
        ON DELETE CASCADE
);

-- ======================
-- ======================
-- Customers
-- ======================
INSERT INTO Customers (name, email, phone, address)
VALUES 
('Sonu Sharma', 'sonu@example.com', '9876543210', '123 MG Road, Bengaluru'),
('Monu Patel', 'monu@example.com', '9123456780', '45 Park Street, Kolkata'),
('Tonu Reddy', 'tonu@example.com', '9988776655', '12 Jubilee Hills, Hyderabad');

-- ======================
-- Products
-- ======================
INSERT INTO Products (name, description, price, stock_qty)
VALUES
('iPhone 15', 'Latest Apple smartphone', 80000, 25),
('Samsung Galaxy S25', 'Flagship Samsung phone', 70000, 30),
('Nike Air Max', 'Running shoes', 5000, 50),
('Levi Jeans', 'Denim pants', 2000, 100),
('Sony Headphones', 'Noise-cancelling headphones', 8000, 40);

-- ======================
-- Orders
-- ======================
-- Order for Sonu
INSERT INTO Orders (cust_id, status, total_amount)
VALUES (1, 'Pending', 85000);

-- Order for Monu
INSERT INTO Orders (cust_id, status, total_amount)
VALUES (2, 'Pending', 7500);

-- ======================
-- OrderItems
-- ======================
-- Sonu's Order (order_id = 1 assumed)
INSERT INTO OrderItems (order_id, prod_id, quantity, price)
VALUES 
(1, 1, 1, 80000),    -- iPhone 15
(1, 5, 1, 5000);     -- Sony Headphones

-- Monu's Order (order_id = 2 assumed)
INSERT INTO OrderItems (order_id, prod_id, quantity, price)
VALUES 
(2, 3, 1, 5000),     -- Nike Air Max
(2, 4, 1, 2000);     -- Levi Jeans

-- ======================
-- Payments
-- ======================
-- Sonu's Payment
INSERT INTO Payments (order_id, amount, method, status)
VALUES (1, 85000, 'Card', 'Successful');

-- Monu's Payment
INSERT INTO Payments (order_id, amount, method, status)
VALUES (2, 7000, 'UPI', 'Pending');

-- ======================
-- Sample Queries
-- ======================
-- Get all customers
SELECT * FROM Customer; 
-- Get all products
SELECT * FROM Product;
-- Get all orders with customer details
SELECT o.order_id, c.name AS customer_name, o.order_date, o.status, o.total_amount
FROM Orders o           
JOIN Customer c ON o.cust_id = c.cust_id;
-- Get order items for a specific order
SELECT oi.order_id, p.name AS product_name, oi.quantity, oi.price
FROM OrderItem oi
JOIN Product p ON oi.prod_id = p.prod_id
WHERE oi.order_id = 1;  -- Replace with desired order_id    
-- Get payments for a specific order
SELECT p.pay_id, o.order_id, p.amount, p.method, p.status, p.paid_at
FROM Payment p  
JOIN Orders o ON p.order_id = o.order_id
WHERE o.order_id = 1;  -- Replace with desired order_id
-- Get total sales amount
SELECT SUM(total_amount) AS total_sales     
FROM Orders
WHERE status = 'Successful';
-- Get total stock value
SELECT SUM(price * stock_qty) AS total_stock_value  
FROM Product;

