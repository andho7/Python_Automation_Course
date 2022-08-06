# Є словник з ключами-строками та елементами-списками строк, наприклад:
#
data = {
	'colors': ['red', 'green', 'blue', 'purple'],
	'fruits': ['pineapple', 'orange', 'banana'],
	'clothes': ['coat', 'tshirt']
}
#
# Завдання: перебудувати словник (не створюючи новий) таким чином що
#           його значення стануть ключами значенням котрих буде їхній
#           ключ з початкового словника.
#
# Підказки:
# * dict[key] = value
# * for key in dict
# * for value in dict[key]


for i in data.items():
	key = i[0]
	value = tuple(i[1])
	data.pop(i[0])
	data[value] = key

print(data)


for k, l in data.items():
    for v in l:
        data[v] = k
    



# Output:
# {
# 	('red', 'green', 'blue', 'purple'): 'colors',
# 	('pineapple', 'orange', 'banana'): 'fruits',
# 	('coat', 'tshirt'): 'clothes'
# }



