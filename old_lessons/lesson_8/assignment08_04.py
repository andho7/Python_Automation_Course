# Завдання: написати функцію лінійного пошуку елементу у послідовності.
#           На вхід подається послідовніть (iterable: list, tuple, str)
#           як перший аргумент, та елемент який потрібно знайти у 
#           послідовності (другим елементом). Результатом виконання 
#           функції буде індекс першого елементу (якщо такий елемент
#           знайдено) чи None (у разі якщо у послідовності відсутній
#           потрібний елемент.
#
#           Послідовність може вводитися користувачем, або рандомною
#           генерацією, або просто використати літеральні послідовності
#           надані безпосередньо у коді (бажано надати приклади з
#           використанням різних типів послідовностей та елементів,
#           пошук літер у строках, чисел у послідовностях чисел, слів
#           у списку слів).
#
#           Лінійний пошук: це перебір елементів послідовності зліва
#           направо, по одному, до тих пір поки не знайдено потрібний
#           елемент, або, якщо такий відсутній, - більше немає елементів
#           у послідовності.
#
# Приклад:
#
#         s = "Hello world"
#         print(linear_search(s, "w"))  # prints: 6
#         print(linear_search(s, "W"))  # prints: None
#         words = ["Hello", "world"]
#         print(linear_search(words, "planet")  # prints: None
#         nums = tuple(range(10))
#         print(nums, 3)  # prints: 4
#

def linear_search(iterable, element):
    # if element in iterable:
    #     return iterable.index(element)
    for i in range(len(iterable)):
        if iterable[i] == element:
            return i
    return None
            
s = "Hello world"
print(linear_search(s, "w"))

words = ["Hello", "world"]
print(linear_search(words, "planet"))

nums = tuple(range(10))
print(linear_search(nums, 0)) 