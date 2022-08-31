"""
Типовое решение заполнения БД данными. Перед выполнением незабываем создать виртуальное окружение!

Будем использовать библиотеку Faker для генерации
случайных данных, в нашем случае имён студентов и преподавателей.
Больше информация - https://faker.readthedocs.io/en/master/index.html
Установка - pip install faker

С библиотекой os вы уже знакомы. Будем использовать для проверки существования файла БД и работы с файлом
скрипта SQL
"""

from datetime import date, datetime, timedelta
from random import randint
import sqlite3
import os
import faker

name_database = 'init_db.db'


def date_range(start: date, end: date) -> list:
    """
    Создаем свою ф-цию для получения списка дат, в которые происходит учебный процесс.
    Для упрощения выбрасываем только дни, которые попадают на выходные.
    """

    result = []
    current_date = start
    while current_date <= end:
        if current_date.isoweekday() < 6:
            result.append(current_date)
        current_date += timedelta(1)
    return result


def create_db(path):
    """
    Функция создания БД, в качестве параметра - передаем путь к файлу с SQL скриптом
    """

    # проверяем на наличие существования БД
    if not os.path.exists(f'{os.path.basename(path).split(".")[0]}.db'):
        # если БД нет - читаем файл со скриптом, переданный в параметре ф-ции
        with open(path) as f:
            sql = f.read()
        # создаем соединение используя менеджер контекста
        with sqlite3.connect(
                f'{os.path.basename(path).split(".")[0]}.db') as conn:
            # создаем объект курсора
            cur = conn.cursor()
            # полностью выполняем скрипт из файла
            cur.executescript(sql)
            # подтверждаем наши действия
            conn.commit()


def fill_data():
    """
    Функция генерации фейковых данных и заполнения ими БД
    """

    # Не все данные будут динамические. Создаем списки предметов и групп
    disciplines = ['Вища математика', 'Хімія', 'Економіка',
                   'Теоретична механіка', 'Менеджмент організацій']

    groups = ['ВВ1', 'ДД33', 'АА5']

    # Создаем объект библиотеки Faker. В качестве параметра передаем локаль
    # Больше - https://faker.readthedocs.io/en/master/locales.html
    fake = faker.Faker('uk-UA')
    # создаём соединение, можно
    conn = sqlite3.connect(name_database)
    # создаем курсор
    cur = conn.cursor()

    #
    try:

        teachers = []  # создаем пустой список преподавателей

        # заполняем его случайными именами из объекта fake
        # range принимает в качестве параметра кол-во требуемых объектов
        for _ in range(3):
            teachers.append(fake.name())

        # создаём переменную с текстом запроса для заполнения таблицы teachers
        sql_teachers = 'INSERT INTO teachers (teacher) VALUES (?)'

        # выполняем запрос используя функцию executemany объекта cursor
        # https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executemany
        cur.executemany(sql_teachers, zip(teachers, ))

        # создаём переменную с текстом запроса для заполнения таблицы disciplines
        sql_disc = 'INSERT INTO disciplines (discipline, teacher) VALUES (?, ?)'

        cur.executemany(sql_disc, zip(
            disciplines, iter(randint(1, 3) for _ in range(len(disciplines)))))

        # создаём переменную с текстом запроса для заполнения таблицы groups
        # так как для SQLite group - зарезервированное слово, берем его в [] для использования
        sql_groups = 'INSERT INTO groups ([group]) VALUES (?)'

        cur.executemany(sql_groups, zip(groups, ))

        students = []  # создаем пустой список студентов

        # заполняем его случайными именами из объекта fake
        for _ in range(30):
            students.append(fake.name())

        sql_students = 'INSERT INTO students (student, [group]) VALUES (?,?)'

        cur.executemany(sql_students, zip(students, iter(randint(1, 3)
                                                         for _ in range(len(students)))))

        # для заполнения таблицы grades нам нужны даты, в которые происходит обучение
        # используем ф-цию date_range, это аналог из библиотеки pandas для генерации дат
        # больше - https://pandas.pydata.org/docs/reference/api/pandas.date_range.html

        # дата начала учебного процесса
        start_date = datetime.strptime("2020-09-01", "%Y-%m-%d")
        # дата окончания учебного процесса
        end_date = datetime.strptime("2021-05-25", "%Y-%m-%d")
        d_range = date_range(start=start_date, end=end_date)

        # создаём пустой список, в котором будем генерировать записи с оценками для каждого студента
        grades = []

        for d in d_range:  # пройдемся по каждой дате
            # Случайно выберем id одного предмета. Считаем, что в один день у нас один предмет
            r_disc = randint(1, 5)
            # допустим, что в один день могут ответить только три студента
            # выбираем троих из наших 30.
            r_students = [randint(1, 30) for _ in range(3)]
            # проходимся по списку "везучих" студентов, добавляем их в результирующий список
            # и генерируем оценку
            for student in r_students:
                grades.append((student, r_disc, d.date(), randint(1, 12)))

        sql_ratings = 'INSERT INTO grades (student, discipline, date_of, grade) VALUES (?, ?, ?, ?)'

        cur.executemany(sql_ratings, grades)

        conn.commit()

    except sqlite3.IntegrityError as e:
        print(e)

    finally:
        conn.close()


if __name__ == '__main__':
    create_db('init_db.sql')
    fill_data()
