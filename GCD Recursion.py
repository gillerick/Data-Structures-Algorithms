"""Assuming x is the larger, the GCD of x and y is the GCD of y and x - y"""
def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


print(gcd(127837949454, 4))
