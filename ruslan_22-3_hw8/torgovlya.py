import sqlite3
from sqlite3 import Error



def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except Error:
        print(Error)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error:
        print(Error)

def create_product(conn, product):
    try:
        sql = '''INSERT INTO products 
        (product_title, price, quantity) 
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error:
        print(Error)

def create_products(conn):
        try:
            create_product(conn, ("Квас", 60.5, 4))
            create_product(conn, ("Садачок", 145.4, 6))
            create_product(conn, ("WinsTan", 110.5, 28))
            create_product(conn, ("Хлеб", 24.5, 27))
            create_product(conn, ("Майонез", 25.5, 25))
            create_product(conn, ("Кофе", 15.5, 30))
            create_product(conn, ("Кефир", 60.5, 21))
            create_product(conn, ("Какао", 75.5, 37))
            create_product(conn, ("Levil", 350.5, 20))
            create_product(conn, ("Coca-Cola", 120.5, 45))
            create_product(conn, ("Fanta", 45.5, 12))
            create_product(conn, ("Pepsi", 110.5, 20))
            create_product(conn, ("AlpenGold", 70.6, 16))
            create_product(conn, ("Супер-Контик", 35.3, 20))
            create_product(conn, ("Lays", 75.5, 20))
        except Error:
            print(Error)

def update_product_quantity(conn, product):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error:
        print(Error)

def update_product_price(conn, product):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error:
        print(Error)


def delete_products(conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except Error:
        print(Error)

def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)

        product_list = cursor.fetchall()
        for product in product_list:
            print(product)
    except Error:
        print(Error)

def select_all_products_by_quantity_and_price(conn):
    try:
        sql = '''SELECT * FROM products WHERE quantity > 5 and price < 100.00'''
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        print(rows)
    except Error:
        print(Error)

def search_by_word(conn, word):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
        cursor = conn.cursor()
        cursor.execute(sql, ('%' + word + '%',))

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error:
        print(Error)



connection = create_connection("hw.db")

create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price DOUBLE (10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER NOT NULL DEFAULT 0
)
'''
if connection is not None:
    print("Connected Success!")





    # create_table(connection, create_products_table)
    #create_products(connection)
    #select_all_products(connection)








