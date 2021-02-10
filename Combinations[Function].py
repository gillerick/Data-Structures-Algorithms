# Function to create combinations
# without itertools
even = [2, 4]
odd = [1, 3, 5]


def combinations():
    l = []
    for i in range(0, len(odd)):
        m = odd[i]
        l.append([m] + [e for e in even if e < m])
    # print(l)

    for j in range(0, len(even)):
        n = even[j]
        l.append([n]+[o for o in odd if o < n])
    print(l)


print(combinations())
