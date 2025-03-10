SELECT Users.ID, Expenses.Amount
FROM Users
JOIN Expenses ON Users.ID = Expenses.User_ID;

SELECT SUM(Expenses.Amount) AS Total_Expenses, Users.Username
FROM Users
JOIN Expenses ON Users.ID = Expenses.User_ID
GROUP BY Users.Username;

SELECT SUM(Expenses.Amount), Categories.Name
FROM Expenses
JOIN CATEGORIES ON Expenses.Category_ID = Categories.ID
GROUP BY Categories.Name;

SELECT Users.Username, SUM(Expenses.Amount) AS Total_Expenses
FROM Users
JOIN Expenses ON User.ID = Expenses.User_ID
JOIN Categories ON Expenses.Category_ID = Categories.ID


SELECT Users.Username , Users.ID, SUM(Expenses.Amount) AS Total_Expenses
FROM Users
JOIN Expenses ON Users.ID = Expenses.User_ID
GROUP BY Users.ID
ORDER BY SUM(Expenses.Amount) DESC;


