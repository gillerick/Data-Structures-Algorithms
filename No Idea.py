"""
Problem link: https://www.hackerrank.com/challenges/no-idea/problem

"""


def happiness():
    happiness_count = 0
    n, m = input().split()
    arr = tuple(map(int, input().split()))
    # arr = input().split()
    a, b = {int(x) for x in input().split()}, {int(y) for y in input().split()}
    for j in arr:
        if j in a:
            happiness_count += 1
        elif j in b:
            happiness_count -= 1

    print(happiness_count)


happiness()
