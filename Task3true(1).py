number = input('Введите число: ')
odds = 0 #Нечет
evens = 0 #Чет

for n in number:
    if int(n) % 2 == 0:
        evens += 1
    else:
        odds += 1
print("\nНечет: {} \nЧет: {}".format(odds, evens))
