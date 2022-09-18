import os
import sqlite3

from typing import List, Set


def execute_query(query_sql: str) -> List:
    """
    Функция для выполнения запроса
    :param query_sql: запрос
    :return: результат выполнения запроса
    """
    db_pass = os.path.join(os.getcwd(), 'chinook.db')
    connection = sqlite3.connect(db_pass)
    cur = connection.cursor()
    result = cur.execute(query_sql)
    return result


def unwrapper(records: List) -> None:
    """
    Функция для вывода результата выполнения запроса
    :param records: список ответа БД
    """
    for record in records:
        print(*record)


def get_employees() -> None:
    """
    Функция получения всех записей из таблицы employees
    """
    query_sql = '''
        SELECT *
          FROM employees;
    '''
    result = execute_query(query_sql)
    unwrapper(result)


def get_FirstName_employees() -> None:
    query_sql = '''
        SELECT FirstName, COUNT(FirstName)
            FROM employees
                GROUP BY FirstName
    '''
    result = execute_query(query_sql)
    unwrapper(result)


print(get_FirstName_employees())
