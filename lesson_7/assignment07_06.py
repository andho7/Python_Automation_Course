"""Задача: написати функцію пошуку елемента у послідовності.

   Деталі:
            * функція приймає два аргумента - послідовність та елемен
            * функція повинна повернути індекс елемента у послідовності
              або -1 якщо не знайдено
            * це аналог функції str.find, list.index
            * написати якийсь код який надає пару прикладів використування

    Приклад:
            * search_linearly([1, 8, 7, 33, 9, 2], 8) -> повертає 1
            * search_linearly("hello world!", "!") -> повертає 11
            * search_linearly(tuple(range(10)), 10) -> повертає -1
"""

def search_linearly(x, y):
  if y in x:
    return x.index(y)
  else:
    return -1


search_linearly([1, 8, 7, 33, 9, 2], 8)
search_linearly("hello world!", "!")
search_linearly(tuple(range(10)), 10)