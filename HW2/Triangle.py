# a = int(input("Введите 1-ое значение: "))
# b = int(input("Введите 2-ое значение: "))
# c = int(input("Введите 3-ое значение: "))
# def trian(*args):
#     p= (a + b + c) / 2
#     square = ((p * (p - a) * (p - b) * (p - c)) ** (1 / 2))
#     print("Площа триугольника =",square)
#
# trian(a, b, c )

a = int(input("Введите 1-ое значение: "))
b = int(input("Введите 2-ое значение: "))
c = int(input("Введите 3-ое значение: "))
# def trian(*args):
#     p= (a + b + c) / 2
#     square = ((p * (p - a) * (p - b) * (p - c)) ** (1 / 2))
#     print("Площа триугольника =",square)
#
# trian(a, b, c )
def rav(*args):
    if a + b > c  and a+c > b and c+b >a:
        return True
    else:
        return False


print(rav(a,b,c))