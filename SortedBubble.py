my_list = [21, 32, 43, 56, 77, 34, 54, 67,98,533,422]

def bubblesorted(my_list):
    for number in range(len(my_list)-1,0,-1):
        for i in range(number):
            if my_list[i]>my_list[i + 1]:
                aft = my_list[i]
                my_list[i] = my_list[i + 1] #смотреть на 11 строку,или так, или так
                my_list[i + 1] = aft

#my_list[i], my_list[i + 1] = my_list[i + 1], aft

bubblesorted(my_list)
print(my_list)


