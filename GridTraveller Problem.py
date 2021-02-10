"""
This is the classical solution of the grid traveller problem
"""


def gridTraveler(n, m):
    if n == 0 or m == 0:
        return 0
    if n == 1 and m == 1:
        return 1
    return gridTraveler(n-1, m) + gridTraveler(n, m-1)


print(gridTraveler(1, 1))
print(gridTraveler(2, 3))
print(gridTraveler(3, 2))
print(gridTraveler(3, 3))

