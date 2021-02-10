"""
There is a horizontal row of  cubes. The length of each cube is given. You need to create a new vertical pile of cubes.
The new pile should follow these directions: if  is on top of  then .

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time.
Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.

"""
from typing import List

numbers: List[List[int]] = []


def pile():
    n = int(input())
    for i in range(n):
        sides = input()
        m = list(map(int, input().split()))
        numbers.append(m)
    # print(numbers)


def checker():
    for n in range(len(numbers)):
        if numbers[n][0] < numbers[n][-1]:
            print("No")
        else:
            del numbers[n][0]
            del numbers[n][-1]
    print("Yes")

print(pile())
