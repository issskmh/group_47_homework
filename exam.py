import sqlite3



def display_stores(cursor):

    cursor.execute("SELECT store_id, title FROM store")
    stores = cursor.fetchall()
    print("Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")
    for store in stores:
        print(f"{store[0]}. {store[1]}")
    print()

def display_products_by_store_id(cursor, store_id):
    cursor.execute("""
        SELECT products.title, categories.title, products.unit_price, products.stock_quantity
        FROM products
        JOIN categories ON products.category_code = categories.code
        WHERE products.store_id = ?
    """, (store_id,))
    products = cursor.fetchall()

    if products:
        for product in products:
            print(f"Название продукта: {product[0]}")
            print(f"Категория: {product[1]}")
            print(f"Цена: {product[2]}")
            print(f"Количество на складе: {product[3]}")
            print()
    else:
        print("Нет продуктов в этом магазине.\n")

def main():
    conn = sqlite3.connect(r'C:\Users\islam\sql hw\exam.db')
    cursor = conn.cursor()

    while True:
        display_stores(cursor)
        try:
            store_id = int(input("Введите id магазина для отображения продуктов или 0 для выхода: "))
        except ValueError:
            print("Пожалуйста, введите допустимое число.\n")
            continue

        if store_id == 0:
            print("Выход из программы.")
            break
        else:
            display_products_by_store_id(cursor, store_id)


    conn.close()

if __name__ == "__main__":
    main()