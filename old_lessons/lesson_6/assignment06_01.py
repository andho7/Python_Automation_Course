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

word_list = text.split()

stat_dict = {'Number of words': len(word_list), 'Number of unique words': len(set(word_list))}

unique_charachter_list = []
letter_occurs_dict = {}

word_occurs_dict = {}
for word in word_list:
	if word not in word_occurs_dict:
		word_occurs_dict[word] = f'{text.count(word)} times'
	for i in word:
		if i not in unique_charachter_list:
			unique_charachter_list.append(i)
		if i not in letter_occurs_dict:
			letter_occurs_dict[i] = f'{unique_charachter_list.count(i)} times'
  
stat_dict['Word occurs'] = word_occurs_dict

stat_dict['Letter occurs'] = letter_occurs_dict

print(stat_dict)