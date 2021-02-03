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
    print(numbers)

    for m in range(len(numbers)):
        if numbers[m][0] < numbers[m][-1]:
            print("No")
            continue
        else:
            del numbers[m][0]
            del numbers[m][-1]
            print("Yes")

print(pile())
