
S = "Forget CVs..Save time . x x"
count = 0
C = []
def solution(S):
    k = S.split('.')
    for i in range(len(k)):
        j = k[i].split()
        C.append(len(j))
        maximum = max(C)
    print(maximum)
    # maximum = C[0]
    # for i in range(len(C)):
    #     if C[i] > maximum:
    #         maximum = C[i]
    #     else:
    #         maximum = C[0]
    # return maximum
    # # print(maximum)


solution(S)
