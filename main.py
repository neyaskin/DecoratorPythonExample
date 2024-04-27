# Пример 1
# def decorator(hello):
#     return hello
#
#
# def hello():
#     print("Hello")
#
# decorator(hello())
# hello_msg = decorator(hello)
# hello_msg()


# Пример 2
# def decorator(func):
#     def wrapper():
#         print("Start")
#         func()
#         print("End")
#     return wrapper
#
#
# def hello():
#     print("Hello")
#
#
# decorator(hello())
# hello_msg = decorator(hello)
# hello_msg()


# Пример 3
# from time import time, sleep
#
#
# def timer(func):
#     def wrapper():
#         start_time = time()
#         func()
#         end_time = time()
#         print(f'Время выполнения: {end_time - start_time} сек.')
#     return wrapper
#
#
# @timer
# def unfreeze():
#     sleep(10)
#
#
# @timer
# def get_nums():
#     return [i for i in range(1, 100000000)]


# get_nums()
# unfreeze()


# Пример 4
# def repeat(func):
#     def wrapper():
#         for _ in range(10):
#             func()
#     return wrapper
#
#
# @repeat
# def message():
#     print('Hello')
#
#
# message()


# Пример 5
# def repeat(func):
#     def wrapper(*args, **kwargs):
#         for _ in range(10):
#             func(*args, **kwargs)
#     return wrapper
#
#
# @repeat
# def message(name):
#     print(f'Hello, {name}')
#
#
# message('Semyon')


# Пример 6
# def access(func):
#     def wrapper(*args, **kwargs):
#         if kwargs.get('password') == 'qweasd123':
#             return f'Доступ разрешен. {func(*args, **kwargs)}'
#         else:
#             return f'Доступ запрещен. Введен неверный пароль!'
#     return wrapper
#
#
# @access
# def send_msg(msg, **kwargs):
#     return f'Сообщение: {msg}'
#
#
# user_pass = input('Введите пароль: ')
# res = send_msg('Секретная информация', password=user_pass)
# print(res)


# Пример 7
# def up(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res.upper()
#     return wrapper
#
#
# def warning(func):
#     def wrapper(*args, **kwargs):
#         return f'Вы получили сообщение: {func(*args, **kwargs)}'
#     return wrapper
#
#
# @warning
# @up
# def send_message(gift):
#     return f'Мне подарили {gift}'
#
#
# print(send_message('Котенка'))


# Пример 8
# from functools import wraps
#
#
# def value(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs) + ' руб.'
#     return wrapper
#
#
# @value
# def cost(price):
#     '''Функция показывает стоимость товара'''
#     return f'Стоимость товара: {price}'
#
#
# print(cost(100))
# print(cost.__name__)
# print(cost.__doc__)


# Пример 9
# from functools import wraps
#
#
# def log_func_info(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f'Вызывается функция: {func.__name__}')
#         print(f'Документация: {func.__doc__}')
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @log_func_info
# def add_book(title, author):
#     '''Добавляет книгу в каталог'''
#     if title not in books:
#         books[title] = author
#         print(f'Книга "{title}" автора "{author}" добавлена в каталог')
#
#
# @log_func_info
# def find_book(title):
#     '''Поиск книги в каталоге'''
#     if title in books:
#         print(f'Книга "{title}" найдена в каталоге')
#     else:
#         print(f'Книга "{title}" не найдена в каталоге')
#
#
# books = {}
#
# add_book("Как стать программистом", "С.А. Неяскин")
# find_book("Как стать программистом")
# find_book("Ловим анаконду")