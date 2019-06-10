import re


text = """There was an old lady who swallowed a fly
I dont know why she swallowed a fly perhaps shell die
There was an old lady who swallowed a spider
That wriggled and wiggled and tickled inside her
She swallowed the spider to catch the fly
I dont know why she swallowed a fly perhaps shell die
There was an old lady who swallowed a bird
How absurd to swallow a bird
She swallowed the bird to catch the spider
She swallowed the spider to catch the fly
I dont know why she swallowed a fly perhaps shell die
There was an old lady who swallowed a cat
Fancy that to swallow a cat
She swallowed the cat to catch the bird
She swallowed the bird to catch the spider
She swallowed the spider to catch the fly
I dont know why she swallowed a fly perhaps shell die
There was an old lady who swallowed a dog                               #1
What a hog to swallow a dog                                          #1
She swallowed the dog to catch the cat                               #1
She swallowed the cat to catch the bird
She swallowed the bird to catch the spider
She swallowed the spider to catch the fly
I dont know why she swallowed a fly perhaps shell die
There was an old lady who swallowed a cow
I dont know how she swallowed a cow
She swallowed the cow to catch the dog                                           #1
She swallowed the dog to catch the cat                                         #1
She swallowed the cat to catch the bird
She swallowed the bird to catch the spider
She swallowed the spider to catch the fly
I dont know why she swallowed a fly perhaps shell die
There was an old lady who swallowed a horse
Shes dead of course
"""

def diff(text):
    text = re.split("\W", text)
    d = {}
    for word in text:
        if word in d:  #конкретное слово
            d[word] = d[word] + 1
        else:
            d[word] = 1

    print(d)

diff(text)



#
# text = """She swallowed the bird to catch the spider
# She swallowed the spider to catch the fly  I dont know why she swallowed a fly perhaps shell die \nThere was an old lady who swallowed a cat
# """

# def dif(text):
#     text = list(text)
#     d = {}
#     for word in text:
#         if word in d:
#             d[word] = d[word] + 1
#         else:
#             d[word] = 1
#
#     print(d)
#
# dif(text)