# Є словник з ключами-строками та елементами-списками строк, наприклад:
#
from multiprocessing.sharedctypes import Value


data = {
	'colors': ['red', 'green', 'blue', 'purple'],
  	'fruits': ['pineapple', 'orange', 'banana'],
  	'clothes': ['coat', 'tshirt']
}
#
# Завдання: перебудувати словник таким чином що
#           його значення стануть ключами значенням котрих буде їхній
#           ключ з початкового словника. Вирішити за допомогою dict
#           comprehensions.


data = { value: key for key, l in data.items() for value in l }

print(data)

# output:
# {'red': 'colors', 'green': 'colors', 'blue': 'colors', 'purple': 'colors', 'pineapple': 'fruits', 'orange': 'fruits', 'banana': 'fruits', 'coat': 'clothes', 'tshirt': 'clothes'}
