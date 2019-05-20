listed = [21, 234,43, 54, 34, 23,33, 45, 67, 3, 6,]

def insertion_sorted(listed):
    for number in range(1, len(listed)):
        value = listed[number]
        i = number - 1
        while i >= 0:
            if value < listed[i]:
                listed[i+1] = listed[i]
                listed[i] = value
                i = i - 1
            else:
                break

insertion_sorted(listed)
print(listed)





