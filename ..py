import sqlite3

db_name = '''group_47.db'''


def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except sqlite3.Error as error:
        print(error)
    return connection


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as error:
        print(error)

def create_table(sql):
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
    except sqlite3.Error as error:
        print(error)


def insert_employee(employee):
    sql = '''INSERT INTO employees (full_name, salary, hobby, birth_date, is_married) 
    VALUES (?, ?, ?, ?, ?)'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, employee)
    except sqlite3.Error as error:
        print(error)


def update_employee(employee):
    sql = '''UPDATE employees SET salary = ?, is_married = ? WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, employee)
    except sqlite3.Error as error:
        print(error)


def delete_employee(id):
    sql = '''DELETE FROM employees WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (id,))
    except sqlite3.Error as error:
        print(error)


def select_all_employees():
    sql = '''SELECT * FROM employees'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as error:
        print(error)


def select_employees_by_salary(salary_limit):
    sql = '''SELECT * FROM employees WHERE salary >= ?'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (salary_limit,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as error:
        print(error)


sql_to_create_employees_table = '''
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name VARCHAR(200) NOT NULL, 
    salary FLOAT(10,2) NOT NULL DEFAULT 0,
    hobby TEXT DEFAULT NULL,
    birth_date DATE NOT NULL,
    is_married BOOLEAN DEFAULT FALSE
)
'''

# my_connection = create_connection(db_name)
# if my_connection is not None:
#     print('Connected to database')
#     create_table(my_connection, sql_to_create_employees_table)
#     my_connection.close()

# create_table(sql_to_create_employees_table)
# insert_employee(('Jim Smith', 1700.5, 'Programming', '2000-01-15', True))
# insert_employee(('Mark Daniels', 1500.0, 'Football', '1999-01-02', False))
# insert_employee(('Alex Brilliant', 2300.5, None, '1989-12-31', True))
# insert_employee(('Diana Julls', 1800.0, 'Programming', '2005-01-22', True))
# insert_employee(('Michael Corse', 1800.0, 'Football', '2001-09-17', True))
# insert_employee(('Jack Moris', 2100.2, 'Programming', '2001-07-12', True))
# insert_employee(('Viola Manilson', 1750.82, None, '1991-03-01', False))
# insert_employee(('Joanna Moris', 1000.0, 'Football', '2004-04-13', False))
# insert_employee(('Peter Parker', 2000.0, 'Programming', '2002-11-28', False))
# insert_employee(('Paula Parkerson', 800.09, None, '2001-11-28', True))
# insert_employee(('George Newel', 1320.0, 'Programming', '1981-01-24', True))
# insert_employee(('Miranda Alistoun', 2500.55, 'Football', '1997-12-22', False))
# insert_employee(('Valeria Hillton', 2000, 'Football', '1977-10-28', True))
# insert_employee(('Jannet Miler', 2100.9, 'Programming', '1997-02-02', True))
# insert_employee(('William Tokenson', 1500, None, '1999-12-12', False))
# insert_employee(('Shanty Morani', 1200.6, None, '1989-08-13', False))
# insert_employee(('Fiona Giordano', 900.12, 'Football', '1977-01-15', True))

# update_employee((2000, False, 2))
# delete_employee(2)

# select_all_employees()
select_employees_by_salary(1500)