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
        for j, k in zip(range(0, len(numbers[m])//2), range(-1, -(len(numbers[m])//2), -1)):
            if numbers[m][j] < numbers[m][k]:
                print("No")
                break
            else:
                print("Yes")

print(pile())
