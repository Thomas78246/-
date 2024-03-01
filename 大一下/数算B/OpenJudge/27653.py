def gcd(x, y):
    if y==0:
        x, y = y, x
    while y != 0:
        y, x = x%y, y
    return x


class Fraction:
    def __init__(self, upper, lower):
        self.upper = upper
        self.lower = lower
        self.simplify()

    def __str__(self):
        return f"{self.upper}/{self.lower}"

    def __add__(self, other):
        n_lower = self.lower * other.lower
        n_upper = self.upper * other.lower + other.upper * self.lower
        return Fraction(n_upper, n_lower)

    def simplify(self):
        common = gcd(self.upper, self.lower)
        self.upper //= common
        self.lower //= common

data = [int(i) for i in input().split()]
f1 = Fraction(data[0], data[1])
f2 = Fraction(data[2], data[3])
fs = f1 + f2
print(fs)
