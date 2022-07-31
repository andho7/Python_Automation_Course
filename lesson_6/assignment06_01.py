# зчитати ввод від користувача - речення (текст) - та порахувати кожне слово у реченні,
# кількість разів воно зустрічається у реченні. Також порахувати статистику використаних
# літер. Для зберігання статистик використати словники.
#
# Підказки:
# * input
# * str.split
# * for word in sequence
# * if key in dict
# * if key not in dict


# 2 порахувати кожне слово в реченні
# 3 скільки разів зустрічається слово в реченні
# 4 порахувати статистику використаних літер

text = input('Введіть речення: ')
# text: str = 'aaaaaaasdf dfg fgh asdf f d p p p p f'
word_list = text.split(' ')

stat_dict = {'Number of words': len(word_list), 'Number of unique words': len(set(word_list))}

word_occurs_dict = {}
for word in word_list:
	if word not in word_occurs_dict.keys():
		word_occurs_dict[word] = f'{text.count(word)} times'
stat_dict['Word occurs'] = word_occurs_dict

letter_occurs_dict = {}
string_of_letters = text.replace(' ', '')
unique_letters_list = []

for i in string_of_letters:
	if i.isalpha():
		unique_letters_list.append(i)

for i in unique_letters_list:
	if i not in letter_occurs_dict.keys():
		letter_occurs_dict[i] = f'{unique_letters_list.count(i)} times'
stat_dict['Letter occurs'] = letter_occurs_dict

print(stat_dict)

# Input
# 'aaaaaaasdf dfg fgh asdf f d p p p p f'
# Output
# {
# 	'Number of words': 11,
# 	'Number of unique words': 7,
# 	'Word occurs': {
# 		'aaaaaaasdf': '1 times',
# 		'dfg': '1 times',
# 		'fgh': '1 times',
# 		'asdf': '2 times',
# 		'f': '6 times',
# 		'd': '4 times',
# 		'p': '4 times'
# 	},
# 	'Letter occurs': {
# 		'a': '8 times', 's': '2 times', 'd': '4 times', 'f': '6 times', 'g': '2 times', 'h': '1 times', 'p': '4 times'
# 	}
# }