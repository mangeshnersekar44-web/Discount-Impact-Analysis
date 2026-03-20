-- Active: 1772520994257@@127.0.0.1@3306@discount_project
-- =========================================
-- 📌 4. BASIC ANALYSIS
-- =========================================

-- Total Revenue
SELECT SUM(Revenue) AS total_revenue
FROM discount_analysis;

-- Total Orders
SELECT COUNT(*) AS total_orders
FROM discount_analysis;

-- Average Discount
SELECT AVG(Discount_Percent) AS avg_discount
FROM discount_analysis;

-- =========================================
-- 📌 . REVENUE ANALYSIS
-- =========================================

-- Revenue by Discount
SELECT Discount_Percent, SUM(Revenue) AS total_revenue
FROM discount_analysis
GROUP BY Discount_Percent
ORDER BY Discount_Percent;



-- Revenue by Category
SELECT Product_Category, SUM(Revenue) AS revenue
FROM discount_analysis
GROUP BY Product_Category
ORDER BY revenue DESC;

-- Revenue by Region
SELECT Region, SUM(Revenue) AS revenue
FROM discount_analysis
GROUP BY Region;

-- =========================================
-- 📌 . CUSTOMER ANALYSIS
-- =========================================

SELECT Customer_Type,
       COUNT(*) AS total_orders,
       AVG(Discount_Percent) AS avg_discount,
       SUM(Revenue) AS total_revenue
FROM discount_analysis
GROUP BY Customer_Type;

-- =========================================
-- 📌 7. DISCOUNT IMPACT ANALYSIS
-- =========================================

-- Discount vs Quantity Sold
SELECT Discount_Percent,
       AVG(Quantity_Sold) AS avg_quantity
FROM discount_analysis
GROUP BY Discount_Percent
ORDER BY Discount_Percent;

-- Discount vs Revenue
SELECT Discount_Percent,
       SUM(Revenue) AS total_revenue
FROM discount_analysis
GROUP BY Discount_Percent
ORDER BY Discount_Percent;



-- =========================================
-- 📌 . ADVANCED ANALYSIS
-- =========================================

-- Top 10 Category + Discount combinations
SELECT Product_Category, Discount_Percent,
       SUM(Revenue) AS revenue
FROM discount_analysis
GROUP BY Product_Category, Discount_Percent
ORDER BY revenue DESC
LIMIT 10;

-- Region + Category Performance
SELECT Region, Product_Category,
       SUM(Revenue) AS revenue
FROM discount_analysis
GROUP BY Region, Product_Category
ORDER BY revenue DESC;

-- =========================================
-- 📌 . CREATE VIEW (FOR DASHBOARD)
-- =========================================

CREATE VIEW revenue_summary AS
SELECT 
    Product_Category,
    Region,
    SUM(Revenue) AS total_revenue,
    AVG(Discount_Percent) AS avg_discount
FROM discount_analysis
GROUP BY Product_Category, Region;

-- Use View
SELECT * FROM revenue_summary;




-- =========================================
-- 📌 . KPI QUERIES (FOR POWER BI)
-- =========================================

-- Top Region
SELECT Region, SUM(Revenue) AS revenue
FROM discount_analysis
GROUP BY Region
ORDER BY revenue DESC
LIMIT 1;

-- Best Category
SELECT Product_Category, SUM(Revenue) AS revenue
FROM discount_analysis
GROUP BY Product_Category
ORDER BY revenue DESC
LIMIT 1;

-- Best Discount %
SELECT Discount_Percent, SUM(Revenue) AS revenue
FROM discount_analysis
GROUP BY Discount_Percent
ORDER BY revenue DESC
LIMIT 1;