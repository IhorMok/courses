# шаг 1 Убрать лишние
# шаг 2 Из строки делаю массив
# шаг 3 выбираю нужные элементы
# шаг 4


collection = ['a', 'b', 'A', 'K', 'V', 'M', 'm']
# word = input()
#collection = input()
k = int((7/10)*100)
print(list([i for i in collection if not i.isupper()]),k,"%")
# k = (4/10)*100
# print(k,"%")