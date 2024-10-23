import sqlite3


def create_database():
    connection = sqlite3.connect('hw.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_title TEXT NOT NULL CHECK(LENGTH(product_title) <= 200),
            price REAL NOT NULL DEFAULT 0.0,
            quantity INTEGER NOT NULL DEFAULT 0
        )
    ''')

    connection.commit()
    connection.close()


def add_products():
    connection = sqlite3.connect('hw.db')
    cursor = connection.cursor()

    products = [
        ('Жидкое мыло с запахом ванили', 50.00, 10),
        ('Мыло детское', 30.00, 20),
        ('Шампунь', 150.00, 15),
        ('Гель для душа', 200.00, 8),
        ('Дезодорант', 100.00, 12),
        ('Крем для рук', 120.00, 5),
        ('Мыло антибактериальное', 45.00, 30),
        ('Шампунь для детей', 70.00, 7),
        ('Бальзам для губ', 20.00, 25),
        ('Гель для мытья посуды', 80.00, 18),
        ('Кондиционер', 160.00, 10),
        ('Мыло с экстрактом алоэ', 55.00, 14),
        ('Туалетная вода', 300.00, 6),
        ('Косметическая маска', 90.00, 16),
        ('Лосьон для тела', 110.00, 9)
    ]

    cursor.executemany('INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)', products)

    connection.commit()
    connection.close()
def update_quantity(product_id, new_quantity):
    connection = sqlite3.connect('hw.db')
    cursor = connection.cursor()

    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, product_id))

    connection.commit()
    connection.close()


def update_price(product_id, new_price):
    connection = sqlite3.connect('hw.db')
    cursor = connection.cursor()

    cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))

    connection.commit()
    connection.close()



def delete_product(product_id):
    connection = sqlite3.connect('hw.db')
    cursor = connection.cursor()

    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))

    connection.commit()
    connection.close()
def print_all_products():
    connection = sqlite3.connect('hw.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()

    for product in products:
        print(product)

    connection.close()
def print_cheap_products(max_price=100.0, min_quantity=5):
    connection = sqlite3.connect('hw.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM products WHERE price < ? AND quantity > ?', (max_price, min_quantity))
    products = cursor.fetchall()

    for product in products:
        print(product)

    connection.close()
def search_products_by_title(search_term):
    connection = sqlite3.connect('hw.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM products WHERE product_title LIKE ?', ('%' + search_term + '%',))
    products = cursor.fetchall()

    for product in products:
        print(product)

    connection.close()
def main():
    create_database()
    add_products()
    print("Все товары:")
    print_all_products()
    print("\nТовары дешевле 100 сом и с количеством больше 5:")
    print_cheap_products()
    print("\nПоиск товаров по названию 'мыло':")
    search_products_by_title('мыло')

    update_quantity(1, 12)  
    update_price(1, 55.00)
    print("\nПосле обновления товара с id=1:")
    print_all_products()

    delete_product(1)
    print("\nПосле удаления товара с id=1:")
    print_all_products()
if __name__ == "__main__":
    main()
