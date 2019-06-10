import functools
@functools.total_ordering

class RomanNumber(int):

    def __init__(self, numbers, system = 10):
        self.numbers = numbers
        self.system = system
        self.values = int(self.numbers, self.system)


    @property
    def clsasses(self):
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thous = ["", "M", "MM", "MMM", "MMMM"]

        t = thous[self.values // 1000]
        h = hunds[self.values // 100 % 10]
        te = tens[self.values // 10 % 10]
        o = ones[self.values        % 10]

        self.numbers =  t + h + te + o
        if self.numbers:
            return self.numbers
        else:
            return float('nan')

    def __add__(self, other):
        return self.values + other


    def __sub__(self, other):
        return self.values - other


    def __eq__(self, other):
        return self.values == other


a = RomanNumber("50")

b = RomanNumber("46")



print(a.clsasses)
print(b.clsasses)


print("The decimal value of",a,"is:")
print(bin(a),"in binary.")
print(oct(a),"in octal.")
print(hex(a),"in hexadecimal.")


