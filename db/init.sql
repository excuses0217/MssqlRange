IF DB_ID('product') IS NULL
    CREATE DATABASE product;
GO

USE product;
GO

IF OBJECT_ID('product', 'U') IS NULL
    CREATE TABLE product (
        id INT PRIMARY KEY IDENTITY(1,1),
        name VARCHAR(255),
        price DECIMAL(10, 2),
        description TEXT
    );
GO

INSERT INTO product (name, price, description) VALUES
('Widget', 15.50, 'A useful widget'),
('Gadget', 22.75, 'A fancy gadget for all your needs'),
('Doodad', 5.00, 'Cheap yet effective');
GO
