"""
Problem link: https://www.hackerrank.com/challenges/no-idea/problem

"""

def happiness():
    # global a, b
    happiness_count = 0
    n, m = input().split()
    arr = input().split()
    a = input().split()
    b = input().split()
    for j, k in zip(a, b):
        if j in arr:
            happiness_count += 1
        if k in arr:
            happiness_count -= 1
        else:
            continue
    print(happiness_count)

happiness()
