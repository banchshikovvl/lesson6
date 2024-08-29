#
#2. Работа со словарями:
my_dict = {'Петров П.П.': 1980, 'Иванов И.И.':1990, 'Сидоров С.С.' :2000}
print(my_dict)
print(my_dict['Петров П.П.'])
print(my_dict.get('Фёдоров Ф.Ф.'))
my_dict.update({'фёдоров Ф.Ф.':2010,'Николаев Н.Н.':2020})
print(my_dict)
a=my_dict.pop('Николаев Н.Н.')
print(a)
print(my_dict)

#3. Работа с множествами:
my_set = {1,1,2,2,3.3,3.3,'four',(5,6,7),True}
print(my_set)
my_set2 ={'six',10,3.14}
my_set.update(my_set2)
print(my_set)
my_set.discard((5,6,7))
print(my_set)