# l = [1, 2, 3, 4, 5]
# def rev(l):
#     new_l = l[::-1]
#     print(new_l)
# rev(l)


l = [1, 2, 3, 4, 5]
def rev(l):
    new_l = []
    for i in range(len(l)-1,-1,-1):
        new_l.append(l[i])
    return new_l
print(rev(l))







# l = [1, 2, 3, 4, 5]
# def reverse(l):
#   l = l[::-1]
#   return l
# print (reverse(l))