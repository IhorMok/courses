#Г ЕНЕРАТОРИ
#iter = (x for x in range(10) if x%2)

# dict1 = {1:0, 2:0, 3:1, 4:2}
# dict2 = {V:K if dict1.values.count() < 2 else [dict1[]]}

# dict1 = {1:0, 2:3, 3:1, 4:2}
# dict2 = {V:K for K,V in dict1.items()}
# print(dict2)
#
#
# dict3 = {1: -1, 2: 2, 3: -3,4: 4}
# dict4 = {K: (V if V > 0 else -V) for K, V in dict3.items()}
# print(dict4)

# list1 = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
# list2 = [x for y in list1 for x in y]
# print(list2)


# list3 = [[x * i for i in range(1,4)] for x in range(1,4)]
# print(list3)

# s = 'abc12'
# num = [int(x) if x.isdigit() else: pass for x in s] # не работает НЕПРАВИЛЬНО
#     print(num)
# num = [int(x) for x in s if x.isdigit()]
# print(num)

# n = int(input())
# def matrix(n):
#     return ([[0 for i in range(n)] for i in range(n)])
# print(matrix(n))

def is_prime(i):
    if i == 2: return True
    for n in range(2, i):
        if i % n == 0: return False
    return True


def primes(n):
    return [x for x in range(2,n+1) if is_prime(x)]
print(primes(35))

