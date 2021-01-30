"""Assuming x is the larger, the GCD of x and y is the GCD of y and x - y"""
def gcd(x, y, cache={}):
    while(x):
        x, y = y, x % y
        return x


print(gcd(127837949454, 4))
