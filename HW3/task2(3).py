import re

k = input('Enter words: ')


def numbers(k):
    vacc = re.split("\D+", k)
    vacc = [i for i in vacc if i != ""]
    return vacc


print(numbers(k))
