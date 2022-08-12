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

# Output:
# {
# 	('red', 'green', 'blue', 'purple'): 'colors',
# 	('pineapple', 'orange', 'banana'): 'fruits',
# 	('coat', 'tshirt'): 'clothes'
# }

a = {1:'a', 2:'b'}
res = dict((v,k) for k,v in a.items())
print(res)
# {'a': 1, 'b': 2}

data = {
	'colors': ['red', 'green', 'blue', 'purple'],
	'fruits': ['pineapple', 'orange', 'banana'],
	'clothes': ['coat', 'tshirt']
}

for k in list(data):
	vs = data.pop(k)
	for v in vs:
		data[v] = k
print(data)

# {'red': 'colors', 'green': 'colors', 'blue': 'colors', 'purple': 'colors', 
#  'pineapple': 'fruits', 'orange': 'fruits', 'banana': 'fruits', 
#  'coat': 'clothes', 'tshirt': 'clothes'}




