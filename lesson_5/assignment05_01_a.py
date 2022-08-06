# Завдання: порахуйте кількість літер строки. Строка та літера
#           даються на вхід користувачем. В залежності від кількости
#           виведіть на екран поясненя: строка містить літеру "с" до 
#           10 разів, строка містить літеру "с" до 20 разid, строка містить
#           символ "c" більше 20 разів. Проінформуйте користувача якщо
#           введено більше ніж одну літеру (літера має довжину більше 1)
#           або повідомляти якщо такої літери взагалі не знайдено.
#
# Підказка:
# * input() - ввод від користувача
# * len(str) - довжина строки
# * str.count(letter) - підрахунок елементів (літер) letter
# * if - elif - else - для логіки виводу на екран
#
# Приклад:
#
# Введіть текст: Це якийсь рандомний текст
# Введіть літеру: й
# Строка містить літеру "й" до 10 разів.
#
# Введіть текст: аааааааааааааааааааааааа
# Введіть літеру: а
# Строка містить літеру "а" більше 20 разів.

random_str = input('Введіть текст: ')
letter = input('Введіть літеру: ')


if len(letter) > 1:
	print('літера має довжину більше 1.')
	exit()
elif len(letter) < 1:
	print('Ви не ввели жодної літери')
	exit()
elif letter not in random_str:
	print(f'Строка не містить літеру "{letter}"')
	exit()
else:
	letter_count = random_str.count(letter)

if letter_count <= 10:
	print(f'Строка містить літеру "{letter}" менше 10 разів.')
elif letter_count <= 20:
	print(f'Строка містить літеру "{letter}" менше 20 разів.')
else:
	print(f'Строка містить літеру "{letter}" ,більше 20 разів.')