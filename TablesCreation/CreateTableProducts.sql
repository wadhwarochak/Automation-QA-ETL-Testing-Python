CREATE TABLE Products (
    ProductID   INT IDENTITY(1,1) CONSTRAINT PK_Products PRIMARY KEY,
    ProductName VARCHAR(100) NOT NULL,
    Category    VARCHAR(50),
    Price       DECIMAL(10,2) NOT NULL CHECK (Price >= 0),
    StockQty    INT DEFAULT 0 CHECK (StockQty >= 0),
    IsActive    BIT DEFAULT 1,
    CreatedDate DATETIME2 DEFAULT SYSDATETIME()
);

INSERT INTO Products (ProductName, Category, Price, StockQty)
VALUES
('Laptop', 'Electronics', 65000.00, 15),
('Wireless Mouse', 'Electronics', 799.50, 120),
('Office Chair', 'Furniture', 8500.00, 20),
('Water Bottle', 'Accessories', 299.00, 200),
('Notebook', 'Stationery', 99.00, 500);
