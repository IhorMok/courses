# #замена пробела между словами на *
# strings = input("Enter any word: ")
# def space(strings):
#     new_strings = strings.replace(" ", "*")
#     return (new_strings)
# print(space(strings),end["*"])


# замена пробела между словами на *
import re

strings = input("Enter any word: ")


def space(strings):

    return re.sub('\s+', '*', strings)


print(space(strings))

# rg = re.compile('\s+')
# rg.sub('a a', '*')

# strings = input("Enter any word: ")
# def space(strings):
#     new_strings = strings.replace(" ", "*")
#     return new_strings
# print(space(strings))
