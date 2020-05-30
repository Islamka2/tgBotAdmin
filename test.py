import sqlite3
import time
# CREATE ADMIN BD
admin_db = sqlite3.connect('admins.db')

sql = admin_db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS admins (
    id INTEGER,
    login TEXT 
    )""")

admin_db.commit()
# ----------------------------

# CREATE USERS BD
users_db = sqlite3.connect('users.db')

user_sql = users_db.cursor()

user_sql.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER,
    login TEXT,
    points INTEGER 
    )""")

users_db.commit()
#

# CREATE LOGS BD
logs_db = sqlite3.connect('logs.db')

logs_sql = logs_db.cursor()

logs_sql.execute("""CREATE TABLE IF NOT EXISTS logs (
    id INTEGER,
    role TEXT,
    login TEXT,
    move TEXT,
    time TEXT
    )""")

logs_db.commit()
done = False

def create_new_admin(admins):
    new_admin_login = str(input("Введите логин: "))
    sql.execute(f"SELECT login FROM admins WHERE login = '{new_admin_login.lower()}'")
    if sql.fetchone() is None:
        for i in sql.execute("SELECT * FROM admins"):
            admins += 1
        sql.execute(f"INSERT INTO admins(id, login) VALUES (?, ?)",(admins,new_admin_login.lower()))
        admin_db.commit()
        print("Новый администратор добавлен, его уникальный ID - ", admins)
    else:
        print("Администратор с таким именем уже есть")

def show_all():
    for login in sql.execute('SELECT * FROM admins'):
        print("ID        LOGIN")
        print(login[0],login[1])


def who_is_you():
    global choice
    choice = int(input("Если вы Администратор введите: 1\nЕсли вы пользователь введите: 2\nВводим... "))
    if choice == 1:
        login = str(input("Введите ваш логин: "))
        check_admin_login(login)
    elif choice == 3:
        choice = 1
        check_admin_password(admin_password)
def check_admin_login(input_login):
    sql.execute(f"SELECT login FROM admins WHERE login = '{input_login.lower()}'")
    # for i in sql.execute(f"SELECT login FROM admins WHERE login = '{input_login.lower()}'"):
    #     print(i)
    if sql.fetchone() is None:
        print("Такого администратора не существует!")
        who_is_you()
    else:
        print("Привет, ", input_login)
        global login
        login = input_login
        check_admin_password(admin_password)


def generate_id(table, name_table):
    table.execute("SELECT * FROM {0}".format(name_table))
    global personal_id
    personal_id = table.fetchall()


def check_admin_password(admin_password):
    password = str(input("Введите пароль: "))
    if password == admin_password:
        print("Добро пожаловать!")
        generate_id(sql, "admins")
        print(personal_id)
    else:
        print("Вы ввели неверный пароль!")
        check_admin_password(admin_password)

admin_password = 'admin'

while not done:
    who_is_you()
    while choice == 1:
        admins = 0
        move = int(input("Что будем делать?\nДобавить нового администратора - 1.\nПосмотреть список администрации - 2.\nВведите номер действия..."))
        if move == 1:
            create_new_admin(admins) 
        elif move == 2:
            show_all()
            result = time.localtime()
            time = "{0}.{1}.{2}. в {3}:{4}:{5}".format(result.tm_mday,result.tm_mon,result.tm_year,result.tm_hour,result.tm_min,result.tm_sec)
            print(time)
        else:
            print("Вы ввели что-то непонятное!") 
    while choice == 2:
        a = input("ты никто!") 
    
