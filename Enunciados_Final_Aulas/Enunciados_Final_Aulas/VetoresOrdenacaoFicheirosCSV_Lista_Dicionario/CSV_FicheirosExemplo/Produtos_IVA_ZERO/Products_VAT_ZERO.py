
# Write a program that creates a MySQL Lite database ProductsZeroIVA.db with the following
# tables:
# 3) Categories (IDCategory, Category) – To store the categories (Vegetables, Fruits, …)
# 4) Products (IDProduct, Name, Price, IDCategory) – Product price list


import sqlite3

class ProductsZeroIVA:
    def __init__(self):
        # create databse: ProductsZeroIVA.db
        self.con = sqlite3.connect("ProductsZeroIVA.db")
        self.cur = self.con.cursor()

        self.con.execute('''CREATE TABLE IF NOT EXISTS Categories
                      (IDCategory INT PRIMARY KEY NOT NULL,
                       Category TEXT NOT NULL);''')
        self.con.execute('''CREATE TABLE IF NOT EXISTS Products
                      (IDProduct INT PRIMARY KEY NOT NULL,
                       Name TEXT NOT NULL,
                       Price Real not null,
                       IDCategory int not null);''')
    def GetTableNames(self):
        # see the tables and structure
        res = self.cur.execute("""SELECT name FROM sqlite_master 
                           WHERE type='table'""")
        print(res.fetchall())


    def InsertData(self):
        data = [(1, 'Hortícolas'),
                (2, 'Frutas'),
                (3, 'Cereais e tubérculos'),
                (4, 'Leguminosas'),
                (5, 'Carne, peixe e ovos'),
                (6, 'Laticínios e similares'),
                (7, 'Gorduras e Óleos')
        ]
        self.cur.executemany("INSERT INTO Categories VALUES(?, ?)", data)
        self.con.commit()

        data = [(1, 'Tomate', 1.23, 1),
                (2, 'Cauliflower', 0.0, 1),
                (3, 'Lettuce', 0.0, 1),
                (4, 'Broccoli', 0.0, 1),
                (5, 'Carrot', 0.0, 1),
                (6, 'Courgette', 0.0, 1),
                (7, 'Garlic - French', 0.0, 1),
                (8, 'Pumpkin', 0.0, 1),
                (9, 'turnip', 0.0, 1),
                (10, 'greens', 0.0, 1),
                (12, 'Cabbage', 0.0, 1),
                (13, 'Portuguese', 0.0, 1),
                (14, 'spinach', 0.0, 1),
                (15, 'Turnip', 0.0, 1),

                (16, 'Litter', 0.85, 2),
                (17, 'Banana', 1.45, 2),
                (18, 'Orange', 1.2, 2),
                (19, 'Pear', 1.4, 2),
                (20, 'Melon', 2.4, 2),

                (21, 'Bread', 0.0, 3),
                (22, 'Potato', 0.0, 3),
                (23, 'Pasta', 0.0, 3),
                (24, 'Rice', 0.0, 3),
                (25, 'Gluten - free products for celiac patients', 0.0, 3),

                (26, 'Red bean', 0.0, 4),
                (27, 'Cowpea', 0.0, 4),
                (28, 'Chickpea', 0.0, 4),
                (29, 'Peas', 0.0, 4),

                (30, 'Pork', 0.0, 5),
                (31, 'Chicken', 0.0, 5),
                (32, 'Turkey meat', 0.0, 5),
                (33, 'Beef', 0.0, 5),
                (34, 'Cod', 0.0, 5),

                (35, 'Sardine', 0.0, 5),
                (36, 'hake', 0.0, 5),
                (37, 'horse mackerel', 0.0, 5),
                (38, 'canned tuna', 0.0, 5),
                (39, 'Golden', 0.0, 5),
                (40, 'Mackerel', 0.0, 5),
                (41, 'Chicken eggs', 0.0, 5),

                ]

        self.cur.executemany("INSERT INTO Products VALUES(?,?,?,?)", data)
        self.con.commit()


    def ListCategories(self):
        cursor = self.con.execute("SELECT * from Categories")
        for row in cursor:
            print("{:5} {:}".format(row[0],row[1]))

    def ListProducts(self):
        cursor = self.con.execute("SELECT * from Products")
        for row in cursor:
            print("{:5} {:30} {:10} {:}".format(row[0],
                                                row[1][:30],
                                                row[2],
                                                row[3]))
    # 4) Count the products by category
    def ProductsByCategory(self):
        cursor = self.con.execute("SELECT IDCategory, count(*) 'N' "
                                  " from Products"
                                  " group by IDCategory"
                                  " union "
                                  " SELECT 'Total' x, count(*) 'N'"
                                  " from Products")
        for row in cursor:
            print("{:5} {:}".format(row[0], row[1]))

        # v2
        cursor = self.con.execute("SELECT Category, count(*) 'N' "
                                  " from Products, Categories "
                                  " where Products.IDCategory = Categories.IDCategory"
                                  " group by Category")

        print("{:20} {:}".format('Category', 'Count'))
        for row in cursor:
            print("{:20} {:>4}".format(row[0], row[1]))