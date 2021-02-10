"""A bubble sort is often considered the most inefficient sorting method since it must exchange items before the final location is known.
These “wasted” exchange operations are very costly. However, because the bubble sort makes passes through the entire unsorted portion of the list,
it has the capability to do something most sorting algorithms cannot. In particular, if during a pass there are no exchanges,
then we know that the list must be sorted. A bubble sort can be modified to stop early if it finds that the list has become sorted.
This means that for lists that require just a few passes, a bubble sort may have an advantage in that it will recognize the sorted list and stop."""

# Modified Bubble Sort
from time import time


def timer(func):
    def f(*x):
        before = time()
        t = func(*x)
        after = time()
        print(f"Elapsed time: {float(after-before)}")
        return t
    return f


@timer
def shortbubblesort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum-1


alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110, 34445, 6, 6, 76, 65, 43, 34, 4,34454, 32,2, 343, 232, 234, 232, 23, 43,4 , 454 ,232, 232, 232 ,45 , 565, 434]
shortbubblesort(alist)
print(alist)
