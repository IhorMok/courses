#=====task2==========
# cyc = ('A', 'B', 'C', 'D')
# def cycle(*iterable):
#     cyc = ('A', 'B', 'C', 'D')
#     while True:
#         for cyc in iterable:
#             for k in cyc:
#                 yield k
# for k in cycle(cyc):
#     print(k)

# for k in cycle('A', 'B', 'C', 'D'):
#     print(k)



cyc = ('A', 'B', 'C', 'D')
def cycle(iterable):
    while True:
      for k in iterable:
          yield k

for k in cycle(cyc, cyc):
    print(k)