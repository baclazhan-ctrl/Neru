import sqlite3

# Подключаемся к базе данных (или создаем ее, если она не существует)
conn1 = sqlite3.connect('settings.db')

# Создаем курсор
cursor_settings = conn1.cursor()

# SQL-запрос для создания таблицы
cursor_settings.execute('''
        CREATE TABLE IF NOT EXISTS setting (
            value TEXT NOT NULL
        )
    ''')

# Вставляем начальные значения в таблицу
#cursor_settings.execute('INSERT INTO setting (value) VALUES (?)', ('-',))

# Сохраняем изменения
conn1.commit()

def add_mic_to_set(mic):
    conn = sqlite3.connect('settings.db')
    cursor_settings = conn.cursor()

    # SQL-запрос для вставки новой строки в таблицу events
    cursor_settings.execute('''
            UPDATE setting
            SET value = ? 
            WHERE rowid = 1
        ''', (mic,))

    # Сохраняем изменения
    conn.commit()
    cursor_settings.close()

def get_mic():
    conn = sqlite3.connect('settings.db')
    cursor_settings = conn.cursor()

    # SQL-запрос для извлечения первой строки из таблицы
    cursor_settings.execute('SELECT value FROM setting LIMIT 1')

    # Получаем результат (первую строку)
    result = cursor_settings.fetchone()


    cursor_settings.close()
    conn.close()
    return result

def clear_table():
    conn = sqlite3.connect('settings.db')
    cursor_settings = conn.cursor()

    # SQL-запрос для удаления всех записей из таблицы events
    delete_query = 'DELETE FROM setting;'

    # Выполняем SQL-запрос
    cursor_settings.execute(delete_query)

    # Сохраняем изменения
    conn.commit()

def add_output_to_set(output):
    conn = sqlite3.connect('settings.db')
    cursor_settings = conn.cursor()

    # SQL-запрос для вставки новой строки в таблицу events
    cursor_settings.execute('''
            UPDATE setting
            SET value = ? 
            WHERE rowid = 2
        ''', (output,))

    # Сохраняем изменения
    conn.commit()
    cursor_settings.close()
def get_output():
    conn = sqlite3.connect('settings.db')
    cursor_settings = conn.cursor()

    # SQL-запрос для извлечения первой строки из таблицы
    cursor_settings.execute('SELECT value FROM setting LIMIT 2')

    # Получаем результат (первую строку)
    result = cursor_settings.fetchone()


    cursor_settings.close()
    conn.close()
    return result









select_query = 'SELECT * FROM setting;'
# Выполняем SQL-запрос
cursor_settings.execute(select_query)
# Получаем все результаты
rows = cursor_settings.fetchall()
if rows:
    for row in rows:
        print(row)
else:
    print("Таблица 'events' пуста.")

# Закрываем соединение после всех операций
conn1.close()
