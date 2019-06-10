# for i in [1, 2, 3, 4]:
#     print(i)
#
# class Gen:
#     lst = [1, 2, 3, 4]
#     ind = 0
#
#     def __iter__(self):
#         return self.lst
#
#     def __next__(self):
#         if self.ind < len(self.lst):
#             return self.lst[self.ind]
#         else:
#             raise StopIteration
#
#     def __contains__(self, value):
#         return value in self.lst
#
#
# print(1 in Gen)

# g = (x**x for x in range(3))
# # print(list(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# def gen():
#     y1 = yield 'start iter'
#     print(y1)
#     yield 2
#     yield 3
# g = gen()
# print(g.send(None))
# print(g.send("y1"))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))




# def Fib(n):
#     a, b = 0, 1
#     while True:
#         if a <= n:
#             yield a
#             a, b = b, a+b
#         else:
#             break
#
# f = Fib(1000)
#
# for i in f:
#     print(i)

#
# def repeat(n):
#     while True:
#         yield n
#
#
# for i in repeat(2):
#     print(i)



# def chain(*iterable):
#     for it in iterable:
#         for item in it:
#             yield item
#
# for i in chain([1, 2, 3], {4:4, 5:5}):
#     print(i)


# def seq():
#     n = 0
#     while True:
#         yield n
#         n = 4 * n + 3
#
# m = 0
#
# for i in seq():
#     m +=i


# def num():
#     n = yield 1
#     yield 2
#     yield 3
# b = num()
# res = 3 * n - 3
#
# print(b.send(None)




#==========task1========
# def num():
#     n = yield
#     while True:
#         yield n
#         n = 3*n-3
#
# b = num()
#
# print(b.send(None))
# print(b.send(3))
# print(next(b))
# for i in b:
#     if i>50:
#         break
#     print(i)
#========================


#=====task2========== Закинул в файл Cycle.py
cyc = ('A', 'B', 'C', 'D')
def cycle(*iterable):
    cyc = ('A', 'B', 'C', 'D')
    while True:
        for cyc in iterable:
            for k in cyc:
                yield k
for k in cycle(cyc):
    print(k)

# for k in cycle('A', 'B', 'C', 'D'):
#     print(k)