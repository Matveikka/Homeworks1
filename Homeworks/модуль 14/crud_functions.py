import sqlite3
connection = sqlite3.connect('Products.db')
cursor = connection.cursor()
def initiate_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products
    (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users
    (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    """)
initiate_db()

def get_all_products():
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    return products

def add_user(username, email, age):
    cursor.execute(f"INSERT INTO Users (username, email, age, balance ) VALUES(?, ?, ?, ?)",
                   (f'{username}', f'{email}', age, 1000))

def is_included(username):
    check_user = cursor.execute('SELECT * FROM Users WHERE username=?', (username,))
    if check_user.fetchone():
        return True
    else:
        return False

#for i in range(4):
#    cursor.execute("INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)",
#                   (f"{i+1}", f"продукт{i+1}", f"описание{i+1}", f'{(i+1)*100}'))

connection.commit()
