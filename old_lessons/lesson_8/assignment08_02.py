# Завдання: модіфікувати попередне завдання використавши
#          lambda функції.
#
# Приклад:
#         ввод: 32 7 0 10 11 78 9 5 23 99
#         результат: 32 0 10 78
#
# Підказка:
#   * evens = lambda n: n % 2 == 0 (чи можно одразу передати
#                lambda n: n % 2 == 0 у місці виклиу функції
#                другим аргументом - вона одразу присвоїться
#                в аргумент, але не буде доступна після).


import random


lambda_func = lambda x: x % 2 == 0

def filter_sequence(sequence, lambda_func):
    result = []
    for i in sequence:
        if lambda_func(i):
            result.append(i)
    return result


randomlist = []
for i in range(0,50):
    n = random.randint(1,100)
    randomlist.append(n)

print(filter_sequence(randomlist, lambda_func))