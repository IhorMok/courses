#Класы. Синтаксис.

# class Class:
#     @classmethod
#     def class_method(cls):
#         print(cls._name__)
#
#
#
# class P:
#     @property
#     def prop(self):
#         return 1+1
#     p = P()
#     print(p.prop)


# class Square:
#     def __init__(self,a, b):
#         self.a = a
#         self.b = b
#     @staticmethod
#     def S(a, b):
#         return (a+b)*2
#
#     @staticmethod
#     def K(a,b):
#         return a*b
#
#     @property
#     def s(self):
#         return Square.S(self.a, self.b)
#
#     @property
#     def k(self):
#         return Square.K(self.a, self.b)
#
# m = Square(64, 41)
# print("Square: " + str(m.s), ","" " "Perimeter: " + str(m.k))


#ЗАДАНИЕ 2
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(0, 0)
p2 = Point(1, 1)
print(p1.x, p1.y)
print(p2.x, p2.y)
print(Point.__dict__)