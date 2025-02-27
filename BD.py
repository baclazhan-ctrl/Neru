import sqlite3

# Подключаемся к базе данных (или создаем ее, если она не существует)
conn = sqlite3.connect('LLM_Neru.db')

# Создаем курсор
cursor = conn.cursor()

# SQL-запрос для создания таблицы
create_table_query = '''
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time TEXT NOT NULL,
    Neru TEXT NOT NULL,
    user TEXT NOT NULL,
    event TEXT NOT NULL
);
'''

def add_bd(time, neru, user, event):
    # Подключаемся к базе данных
    conn = sqlite3.connect('LLM_Neru.db')

    # Создаем курсор
    cursor = conn.cursor()

    # SQL-запрос для вставки новой строки в таблицу events
    insert_query = '''
    INSERT INTO events (time, Neru, user, event) 
    VALUES (?, ?, ?, ?);
    '''

    # Выполняем SQL-запрос с данными
    cursor.execute(insert_query, (time, neru, user, event))

    # Сохраняем изменения
    conn.commit()
    cursor.close()
    conn.close()
    #print("Новая строка успешно добавлена в таблицу")


def clear_table():
    """
    Очищает все записи из таблицы events.
    """
    # Подключаемся к базе данных
    conn = sqlite3.connect('LLM_Neru.db')
    cursor = conn.cursor()

    # SQL-запрос для удаления всех записей из таблицы events
    delete_query = 'DELETE FROM events;'

    # Выполняем SQL-запрос
    cursor.execute(delete_query)

    # Сохраняем изменения
    conn.commit()
    select_query = 'SELECT * FROM events;'
    # Выполняем SQL-запрос
    cursor.execute(select_query)
    # Получаем все результаты
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    # Закрываем соединение
    conn.close()


# Пример использования функции
# last_events = get_history()
# for event in last_events:
#     time, neru, user, event_description = event
#     print(f"Time: {time}, Neru: {neru}, User: {user}, Event: {event_description}")

select_query = 'SELECT * FROM events;'
# Выполняем SQL-запрос
cursor.execute(select_query)
# Получаем все результаты
rows = cursor.fetchall()
if rows:
    for row in rows:
        print(row)
else:
    print("Таблица 'events' пуста.")


def fivestrok():
    conn = sqlite3.connect('LLM_Neru.db')
    cursor = conn.cursor()
    # Предположим, у вас есть таблица с именем 'my_table'
    # и вы хотите получить последние 5 строк.
    # В этом примере мы предполагаем, что первый столбец - это идентификатор (ID).

    # Получаем последние 5 строк
    cursor.execute('''
        SELECT * FROM events
        ORDER BY rowid DESC
        LIMIT 5
        
    ''')
    row1 = ""
    row2 = ""
    row3 = ""
    row4 = ""
    row5 = ""
    # Извлекаем данные
    last_five_rows = cursor.fetchall()
    last_five_rows = last_five_rows[::-1]

    # Проверяем, что получили 5 строк
    if len(last_five_rows) == 5:
        row1, row2, row3, row4, row5 = last_five_rows
    else:
        for i, row in enumerate(last_five_rows):
            if i == 0:
                row1 = row
            elif i == 1:
                row2 = row
            elif i == 2:
                row3 = row
            elif i == 3:
                row4 = row
            elif i == 4:
                row5 = row
    # Закрываем соединение
    # Теперь вы можете использовать переменные row1, row2, row3, row4, row5
    row1=list(row1)
    row2 = list(row2)
    row3 = list(row3)
    row4 = list(row4)
    row5 = list(row5)
    return row1,row2,row3,row4,row5



