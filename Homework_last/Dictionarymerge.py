d1 = {2: 5, 4: 8, 7: 23, 9: 42, 14: 5}
d2 = {1: 6, 4: 4, 5: 10, 9: 13, 14: 69}
def merge(d1,d2):
    d3 = d1.copy()
    for key in d2:
        if key in d3:
            d3[key] += d2[key] # = d2[key] + d3[key]
        else:
            d3[key] = d2[key]
    return d3
print(merge(d1,d2))


# https://www.youtube.com/watch?v=JbrPobfQ-mQ