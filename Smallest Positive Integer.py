""""
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
"""


def solution(A):
    m = max(A)
    if m < 1:
        return 1

    A = set(A)
    B = set(range(1, m + 1))
    D = B - A
    if len(D) == 0:
        return m + 1
    else:
        return min(D)
