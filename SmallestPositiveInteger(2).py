# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A.sort()
    for item in A:
        next = item + 1
        if next in A and next > A[-2]:
            return next
    return 1
    # return [x for x in sortedArray if x+1 not in sortedArray and x>0]


if __name__=="__main__":
    print(solution([1, 4, 2, 3, 6, 7]))
