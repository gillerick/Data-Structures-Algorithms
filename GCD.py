"""The central idea in finding GCDs of any two numbers is that if y > x, then the GCD of x and y is the GCD of x and y - x
By extension, this implied that the GCD of x and y is y mod x"""


def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)

print(gcd(12, 4))
