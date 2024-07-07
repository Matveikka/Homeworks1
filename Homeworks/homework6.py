my_dict = {'Матвей': 89114354657, 'Маша': 89564738693}
print(my_dict)
print(my_dict['Матвей'])
print(my_dict.get('Арсений', 'Такого номера нет'))
my_dict.update({'Арсений': 89543758435, 'Иван': 89764856794})
del my_dict['Маша']
print(my_dict)
my_set = {1, 2, 3, 1, 2, 3, 4, 1.2, 1.2, 1.3}
print(my_set)
my_set.update({1.4, 1.5, 6})
print(my_set)