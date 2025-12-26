CREATE TABLE Sales (
    SaleID INT IDENTITY(1,1) PRIMARY KEY,
    SaleDate DATE NOT NULL,
    CustomerName VARCHAR(100) NOT NULL,
    ProductName VARCHAR(100) NOT NULL,
    Quantity INT NOT NULL CHECK (Quantity > 0),
    UnitPrice DECIMAL(10,2) NOT NULL CHECK (UnitPrice >= 0),
    TotalAmount AS (Quantity * UnitPrice) PERSISTED,
    CreatedAt DATETIME DEFAULT GETDATE()
);

INSERT INTO Sales (SaleDate, CustomerName, ProductName, Quantity, UnitPrice)
VALUES
('2025-01-01', 'Amit Sharma', 'Laptop', 1, 55000),
('2025-01-02', 'Neha Verma', 'Mobile Phone', 2, 18000),
('2025-01-03', 'Rahul Mehta', 'Tablet', 1, 22000),
('2025-01-04', 'Pooja Singh', 'Keyboard', 3, 1200),
('2025-01-05', 'Suresh Kumar', 'Mouse', 4, 600),
('2025-01-06', 'Anjali Gupta', 'Monitor', 2, 9500),
('2025-01-07', 'Vikas Jain', 'Printer', 1, 16000),
('2025-01-08', 'Kavita Joshi', 'Router', 2, 3500),
('2025-01-09', 'Manish Arora', 'Headphones', 3, 2500),
('2025-01-10', 'Ritu Malhotra', 'Webcam', 2, 4200),

('2025-01-11', 'Deepak Yadav', 'Laptop', 1, 60000),
('2025-01-12', 'Sunita Rana', 'Mobile Phone', 1, 28000),
('2025-01-13', 'Nitin Bansal', 'Power Bank', 5, 1500),
('2025-01-14', 'Preeti Khanna', 'Smart Watch', 2, 12000),
('2025-01-15', 'Alok Mishra', 'Bluetooth Speaker', 2, 8000),
('2025-01-16', 'Swati Kapoor', 'SSD 1TB', 1, 9000),
('2025-01-17', 'Rakesh Saini', 'External HDD', 1, 7000),
('2025-01-18', 'Monika Chawla', 'USB Cable', 6, 300),
('2025-01-19', 'Sanjay Grover', 'Graphics Card', 1, 45000),
('2025-01-20', 'Nisha Agarwal', 'Gaming Chair', 1, 18000),

('2025-01-21', 'Pankaj Tiwari', 'Microphone', 2, 6500),
('2025-01-22', 'Isha Saxena', 'Laptop Stand', 3, 2500),
('2025-01-23', 'Mohit Aggarwal', 'WiFi Extender', 1, 4200),
('2025-01-24', 'Ayesha Khan', 'Mechanical Keyboard', 1, 7200),
('2025-01-25', 'Rohit Malhotra', 'Noise Cancelling Headphones', 1, 32000);

select * from sales;