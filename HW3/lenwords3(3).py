# s = str(input("Enter words: "))
# min(s.split(), key=len)
# print(min(s.split()))

k = (input('Enter words: '))
def minword(k):
    a = min(k.split(), key=len)
    # a = min(k.split())
    return a
print(minword(k))