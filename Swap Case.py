def swap_case(s):
    C = []
    T = s.split()
    for word in T:
        for c in word:
            if c.islower():
                c.swapcase()
                C.append(c.upper())
            else:
                C.append(c.lower())
        C.append(" ")
    return "".join(C)


if __name__ == "__main__":
    s = input()
    # result = swap_case(s)
    print(swap_case(s))
