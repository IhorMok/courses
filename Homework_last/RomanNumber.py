import functools


@functools.total_ordering
class RomanNumber(int):

    def __init__(self, numbers, system=10):
        self.numbers = str(numbers)
        self.system = system
        self.values = int(self.numbers, self.system)

    def __str__(self):
        return self.classes()

    # @property
    def classes(self):
        try:
            assert 1 <= self.values <= 3999
        except:
            raise Exception(f"ERROR Number from 1 to 3999 Your number is: {self.values}")
        else:
            ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
            tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
            hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
            thous = ["", "M", "MM", "MMM", "MMMM"]

            t = thous[self.values // 1000]
            h = hunds[self.values // 100 % 10]
            te = tens[self.values // 10 % 10]
            o = ones[self.values % 10]

            self.numbers = t + h + te + o
            if self.numbers:
                return self.numbers
            else:
                return float('Nan')

    def __add__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.values + other.values)

        if isinstance(other, int):
            return RomanNumber(self.values + other)

    def __sub__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.values - other.values)

        if isinstance(other, int):
            return RomanNumber(self.values - other)

    def __floordiv__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.values // other.values)

        if isinstance(other, int):
            return RomanNumber(self.values // other)

    def __mul__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.values * other.values)

        if isinstance(other, int):
            return RomanNumber(self.values * other)

    def __lt__(self, other):
        if isinstance(other, RomanNumber):
            return self.values < other.values

        if isinstance(other, int):
            return self.values < other

    def __gt__(self, other):
        if isinstance(other, RomanNumber):
            return self.values > other.values
        if isinstance(other, int):
            return self.values > other

    def __eq__(self, other):
        if isinstance(other, RomanNumber):
            return self.values == other.values  # RomanNumber

        if isinstance(other, int):
            return RomanNumber(self.values) == RomanNumber(other)  # other => int

    def __le__(self, other):
        if isinstance(other, RomanNumber):
            return self.values <= other.values

        if isinstance(other, int):
            return RomanNumber(self.values) <= RomanNumber(other)

    def __ge__(self, other):
        if isinstance(other, RomanNumber):
            return self.values >= other.values

        if isinstance(other, int):
            return RomanNumber(self.values) >= RomanNumber(other)

    def __ne__(self, other):
        # left != right ===> left.__ne__(right)
        # def __ne__(self, other)
        if isinstance(other, RomanNumber):
            return self.values != other.values
        if isinstance(other, int):
            return self.values != other


a = RomanNumber(100)
b = RomanNumber(345)
print(a + b)
print(a // 10)
print(b - 10)
print(a)
print(b)
print(b < 4)
assert RomanNumber(1) != RomanNumber(2)
assert RomanNumber(1) != 2
assert RomanNumber(1) == RomanNumber(1)
assert RomanNumber(1) == 1
assert RomanNumber(2) > RomanNumber(1)
assert RomanNumber(2) > 1
assert RomanNumber(2) >= RomanNumber(1)
assert RomanNumber(2) >= RomanNumber(2)
assert RomanNumber(2) >= 1
assert RomanNumber(2) >= 2
assert RomanNumber(1) < RomanNumber(2)
assert RomanNumber(1) < 2
assert RomanNumber(1) <= RomanNumber(2)
assert RomanNumber(2) <= RomanNumber(2)
assert RomanNumber(1) <= 2
assert RomanNumber(2) <= 2
assert RomanNumber(2) + RomanNumber(2) == 4
assert RomanNumber(2) + 2 == 4
assert RomanNumber(2) * RomanNumber(2) == 4
assert RomanNumber(2) * 2 == 4



