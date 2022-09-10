# Завдання: замінити виклик своєї функції (ітерації та фільтрування елеменів)
#           на використання вбудованої функції filter (використати звичайну
#           або lambda функції як фільтруючу - перший аргумент).
#
# Приклад:
#         ввод: 32 7 0 10 11 78 9 5 23 99
#         результат: 32 0 10 78
#
# Підказки:
#    * filter(callable, iterable)
#

import random

# lambda_func = lambda x: x % 2 == 0

# def filter_sequence(sequence, lambda_func):
#     result = []
#     for i in sequence:
#         if lambda_func(i):
#             result.append(i)
#     return result


randomlist = []
for i in range(0,50):
    n = random.randint(1,100)
    randomlist.append(n)

# print(filter_sequence(a, lambda_func))

print(list(filter(lambda x: x % 2 == 0, randomlist)))