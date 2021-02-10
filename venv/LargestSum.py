"""
Take an array with positive and negative integers and
find the maximum sum of that array
"""


def max_sum(array):
    d = set()
    for number in array:
        if number not in d and number > 0:
            d.add(number)
    print(sum(d))


max_sum([7, 1, 2, -1, 3, 4, 10, -12, 3, 21, -19])
