#Строки
# s = 'Hello'
# for char in s:
#     print(char)
# print(s[3])
# h = 'world'
# print(s + h)
# print('hello','world')

# one = 1
# two = 2
# print(f'{one}+{one}={two}') #f string example
# print('\n Hello\n')# сырые string
#
# print(dir ('my name is..'))


# def is_float(st):
#     if '.' in st:
#         return True
#     else:
#         return False
# print(is_float(("1232.56")))

def new_max(funcc):
    def inner():
        print("\n",funcc(),"\n")
    return inner

@new_max
def max_input():
    number = input("Enter number: ")
    number_innn = number.split()
    res = 0
    for i in number_innn:
        if int(i)>res:
            res = int(i)
    return res
max_input()

# def max_input():
#     print(max(map(int, input().split())))
# max_input()
