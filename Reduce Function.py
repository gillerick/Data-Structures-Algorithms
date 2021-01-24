from fractions import Fraction
from functools import reduce


def product(fracs):
    t = reduce(lambda n, d: Fraction(n*n, d*d), [fracs[i] for i in range(len(fracs))])
    return t._numerator, t._denominator


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
    # print(fracs)
