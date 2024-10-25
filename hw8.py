import sqlite3


def main():
    # Укажите путь к вашей базе данных
    db_path = r'C:\Users\islam\sql hw\hw8.db'

    # Подключение к базе данных
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Вывод приветственного сообщения
    print(
        "Вы можете отобразить список учеников по выбранному id города из перечня городов ниже,"
        " для выхода из программы введите 0:")

    # Получение списка городов
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()

    # Вывод списка городов
    for city in cities:
        print(f"{city[0]}: {city[1]}")  # Выводим ID и название города

    while True:
        # Запрос ID города у пользователя
        city_id = int(input("\nВведите ID города (или 0 для выхода): "))

        # Проверка на выход
        if city_id == 0:
            print("Выход из программы.")
            break

        # Получение информации об учениках, проживающих в выбранном городе
        cursor.execute("""
            SELECT s.first_name, s.last_name, c.title, c.area
            FROM students s
            JOIN cities c ON s.city_id = c.id
            WHERE c.id = ?
        """, (city_id,))

        students = cursor.fetchall()

        # Проверка, есть ли ученики в выбранном городе
        if students:
            print("\nСписок учеников:")
            for student in students:
                print(f"Имя: {student[0]}, Фамилия: {student[1]}, Город: {student[2]}, Площадь города: {student[3]}")
        else:
            print("Нет учеников в выбранном городе.")

    # Закрытие соединения
    conn.close()


if __name__ == "__main__":
    main()
