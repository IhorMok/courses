# l = [1, 2, 3, 4, 5,6, 7, 8, 9, 10]
# *a, = (lambda x: x%2, l)

def funct():
    a = []
    a_int = []
    a_float = []
    n = int(input('Enter '))
    for i in range(n):
        inp = input("ENTER: ").split(" ")
        for j in inp:
            if "." in j:
                a_float.append(j)
            else:
                a_int.append(j)

    a_int = list(map(int, a_int))
    a_float = list(map(float, a_float))

    a_int.sort()
    a_float.sort()


    print(a_int, a_float)


funct()

#Доделать!!

"""кількість рядків, які треба зчитати з термінала
вертає відсортований массив ( спочатку цілі числа, потім доповнений дробовими числами)
"""

