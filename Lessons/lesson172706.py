# регулярные выражения import re
import re

# phone1 = '0665610054'
#
# phone2 = '+380665610054'
#
#
# pattern = re.compile(r'((\+38)?[0-9]{10})')
#
# print(pattern.match(phone1).group())

time1 = '11:59'

pattern1 = re.compile(r'(([0-1][0-1]):([0-5][0-9]))')
print(pattern1.match(time1).group())

time2 = '18:27'

pattern2 = re.compile(r'(([0-1][0-9]|2[0-3]):([0-5][0-9]))')
print(pattern2.match(time2).group())

date = '27/06/2019'

pattern3 = re.compile(r'(([0-2][0-9]|3[0-1])/(0[0-9]|1[1-2])/([0-2][0-2][0-2][0-9]))')
print(pattern3.match(date).group())

# print(pattern.findall(phone2))
# print(
#     re.match(r'', phone1).group(),
#     re.match(r'', phone2).group()
# )



# match = "Hello1324"
# string = """
# If you want to be first in line to experience new features, download our latest
# Canary builds available for OSX (x64) / Windows (x86 or x64) / Linux (x86 or x64)
# for a sneak peek. Our Canary builds are designed for early
# adopters, and may sometimes break.
# """
#
#
#
# # re.match()

# result = re.search(r'HI', string)
# print(result.group())


# result = re.findall(r'([bB])\w+', string)  #Слова начинанаються на b и B
# print(result)


# result = re.split(r'\s', string)   #Разбили по \
# print(result)


# result = re.sub(r'\s', '!', string)           #Заменяем символы на что-угодно
# print(result)

#
# pattern = re.compile(r'\(x\d{2}\s?(or)?\s(x\d{2})?\)')
# result = pattern.findall(string)
# # print(result)



