#инкапсуляция.
# class A:
#     a = 'a'
#     def print_self(self):
#             print('A')
#
# class B:
#     b = 'b'
#     def print_self(self):
#             print('B')
#
# class C(A,B):
#     c = 'c'
#     a = 'a1'
#     b = 'b1'
#     def print_self(self):
#         print('c')
#         super().print_self()
# c = C()
# c.print_self()

# c = C()
# print(c.a, c.b, c.c)
# c.print_self()
# print(C.mro())

# super(A, self).f()
# a = 1
# print(type(a))
#
# class A:
#     pass
# print(type(A))


# def singletone(Point):
#     instance = None
#     def inner(*args, **kwargs):
#         nonlocal instance
#         if instance is None:
#             instance = Point(*args, **kwargs)
#         return instance
#     return inner
#
# @singletone
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
# p1 = Point(3, 4)
# p2 = Point(4, 5)
# print(p1 is p2)
#



# def __add__(self, other):
#     if not isinstance(other, Point):



#
class MyDict(dict):
    def __iadd__(self, dicte):
        if isinstance(dicte,[dict,MyDict]):
            return


my_dict = MyDict()
my_dict += {'a':'a', 'x':'x'}
