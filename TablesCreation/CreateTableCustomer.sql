CREATE TABLE Customer (
    CustomerID INT IDENTITY(1,1) PRIMARY KEY,
    FirstName   VARCHAR(50) NOT NULL,
    LastName    VARCHAR(50),
    Email       VARCHAR(100) UNIQUE,
    Phone       VARCHAR(15),
    City        VARCHAR(50),
    CreatedDate DATETIME DEFAULT GETDATE()
);
INSERT INTO Customer (FirstName, LastName, Email, Phone, City)
VALUES
('Aman', 'Verma', 'aman.verma@gmail.com', '9876501234', 'Noida'),
('Pooja', 'Sharma', 'pooja.sharma@gmail.com', '9898012345', 'Chandigarh'),
('Neha', 'Singh', 'neha.singh@gmail.com', '9123456789', 'Gurgaon');
