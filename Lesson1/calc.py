def calculate():
    print("Елементарный калькулятор в Python")
    num1 = int(input("Введите первое число:  "))
    num2 = int(input("Введите второе число:  "))

    k = int(input("Какую операцию желаете выполнить? \n 1 Сложение \n 2 Вычитание \n 3 Деление \n 4 Умножение \n"))

    if k == 1:
        r = num1 + num2
        p = 'сложения'
        t = p
    if k == 2:
        r = num1 - num2
        l = 'вычитания'
        t = l
    if k == 3:
        r = float(num1 / num2)
        m = 'деления'
        t = m
    if k == 4:
        r = num1 * num2
        n = 'умножения'
        t = n
    print('Результат ', t, ' = ', r)

while True:
    calculate()
    b = int(input("Желаете завершить программу?: \n 1.Да,завершить программу \n 2 Нет,повторно посчитать\n"))
    if b == 1:
        exit(0)
