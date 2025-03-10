USE TrackerExpenses_db;
INSERT INTO Users (Username, Password, Email)
VALUES('Sindi Krasniqi', 'sindi123', 'sindi@gamil.com'),
('Lushi Sulka', 'lushi123', 'lushi@gmail.com'),
('Liridon Krasniqi', 'liridon123', 'liridon@gmail.com'),
('Besa Krasniqi', 'besadona123', 'besa@gmail.com');

INSERT INTO Categories(Name)
VALUES('Food'),
('Transport'),
('Entertainment'),
('Clothes'),
('Health'),
('Education'),
('Other');

INSERT INTO Expenses(Amount, Description, Category_ID, User_ID)
VALUES(15.5, "Lunch", 1, 2),
(10, "Bus ticket", 2, 1),
(20, "Cinema", 3, 3),
(50, "Shirt", 4, 4),
(30, "Medicine", 5, 2),
(100, "Books", 6, 1),
(5, "Coffee", 1, 3),
(10, "Taxi", 2, 4),
(40, "Shoes", 4, 2),
(25, "Vitamins", 5, 3),
(80, "Notebooks", 6, 4);

INSERT INTO Budgets(Amount, User_ID)
VALUES(100, 1),
(200, 2),
(300, 3),
(400, 4);