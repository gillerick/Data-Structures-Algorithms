# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Temporary array to store integers
    C = []
    # write your code in Python 3.6
    for i in A:
        if i % 3 == 0:
            C.append(int(i))
        # print(C)
        maximum = C[0]
        # print("Max", maximum)
        for i in range(1, len(C)):
            if C[i] > maximum:
                maximum = C[i]
        print(maximum)

