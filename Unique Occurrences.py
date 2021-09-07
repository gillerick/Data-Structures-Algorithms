def solution(S):
    char_count = {}

    if len(set(S)) < 2:
        return 0

    for char in S:
        keys = char_count.keys()
        if char in keys:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for count in char_count.values():
        if count
    # return char_count



if __name__ == "__main__":
    print(solution('aaabbbaa'))
    print(solution('aaaaaa'))
