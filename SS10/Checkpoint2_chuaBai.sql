USE NorthwindFullData;

-- 1.
-- SELECT Orders.OrderID, Customers.CustomerID, Customers.CustomerName, Customers.Country
-- FROM Orders LEFT JOIN Customers
-- ON Customers.CustomerID = Orders.CustomerID
-- ORDER BY OrderID;

-- 2. 
-- SELECT Customers.Country, COUNT(Orders.OrderID) AS Ordered
-- FROM Orders 
-- LEFT JOIN Customers ON Orders.CustomerID = Customers.CustomerID
-- GROUP BY Customers.Country
-- ORDER BY Ordered DESC;


-- 3. 
-- SELECT Products.ProductID, Products.ProductName, OrderDetails.Quantity, Products.Price
-- FROM OrderDetails 
-- LEFT JOIN Products ON OrderDetails.ProductID = Products.ProductID
-- WHERE OrderDetails.OrderID = 10248;

-- 4.
-- SELECT OrderDetails.OrderID, SUM(Products.Price * OrderDetails.Quantity) AS TotalAmout
-- FROM OrderDetails
-- LEFT JOIN Products ON OrderDetails.ProductID = Products.ProductID
-- WHERE OrderDetails.OrderID = 10248;


-- 5.
-- SELECT Orders.OrderID, SUM(Products.Price * OrderDetails.Quantity) AS TotalAmout
-- FROM OrderDetails
-- LEFT JOIN Products ON OrderDetails.ProductID = Products.ProductID
-- LEFT JOIN Orders ON Orders.OrderID = OrderDetails.OrderID

-- WHERE Orders.OrderDate = '1996-08-01'
-- GROUP BY Orders.OrderID;


-- 6. 
-- SELECT Orders.OrderID, Customers.CustomerID, Orders.OrderDate
-- FROM Orders
-- LEFT JOIN Customers ON Orders.CustomerID = Customers.CustomerID
-- WHERE Customers.Country = 'Argentina' OR Orders.OrderDate < '1996-07-08';

-- 7. 
-- SELECT ProductID, ProductName, Price
-- FROM Products
-- WHERE Price > (SELECT AVG(Price) FROM Products)
-- ORDER BY Price ASC;

-- 8.
-- SELECT Orders.OrderID, Orders.OrderDate, Customers.CustomerID, Products.ProductID, Products.ProductName
-- FROM Customers 
-- JOIN Orders ON Customers.CustomerID = Orders.CustomerID
-- JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
-- JOIN Products ON OrderDetails.ProductID = Products.ProductID

-- WHERE Products.Category = 'Dairy Products'
-- ORDER BY Orders.OrderID ASC;

-- 9.
SELECT DISTINCT Customers.CustomerID, Customers.CustomerName
FROM Customers 
JOIN Orders ON Customers.CustomerID = Orders.CustomerID
JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
JOIN Products ON OrderDetails.ProductID = Products.ProductID
WHERE Products.Category = 'Dairy Products'
ORDER BY Customers.CustomerID ASC;


