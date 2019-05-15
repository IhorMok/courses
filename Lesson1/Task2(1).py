n = input("Число: ")
givenlist = list(n)
givenlist = [int(i) for i in givenlist]
result_sum = sum(givenlist)

givenlist_without_zero = [i for i in givenlist if i != 0]
result_mult = 1
for x in givenlist_without_zero:
    result_mult *= x

print(result_mult)
print(result_sum)
