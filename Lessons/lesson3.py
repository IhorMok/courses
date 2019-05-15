# def star_print(f):
#     def inner():
#         print("HHHHHHH")
#         f()
#         print("IIIIIIII")
#     return inner
# @star_print
# def f():
#     print("Hiii")
# f()

# def mul2(func):
#     def inner(*arg):
#         r = func(*arg)
#         return 2*r
#     return inner
# @mul2
# def f (a,b):
#     return a+b      #====== mul2(f)(3,3)
# print(f(3,3))

# def mul(a):
#     def inner(b):
#         return a*b
#
#     return inner
# mul2 = mul(2)
# print(mul2(2))
#print(mul2(2)) == mul(2)=a  (2)=b


# def counter(f):
#     count=0
#     def inner(*arg, **kwargs):
#         nonlocal count
#         count += 1
#         f(*arg,**kwargs)
#         inner.count = count #атрибут count который ссылаеться на счетчик  count
#     return inner
# @counter
# def p():
#     print("hi")
# p()
# p()
# p()
# print(p.count)
# p = p.__closure__[0]
# print(p.cell_contents)

# def dec (f):
#     def inner(*args):
#         f()
#         print("Score: ", *args)
#         b = f()
#         return b
#     return inner
# @dec
# def f(*args):
#     print("value")
#
#
# f(3, 4, 5, 7)

def is_b_zero(f):
    def inner(a,b):
        if b == 0:
            print("B shoudnt = 0")
        else:
            c = f(a,b)
            return c
    return inner
@is_b_zero
def f(a,b):
    print(a/b)
f(4,9)