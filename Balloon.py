def solution(S):
    balloon = {'B': 0, 'A': 0, 'L': 0, 'O': 0, 'N': 0}

    # store frequencies of relevant letters in a hashmap
    for letter in S:
        if letter in balloon:
            balloon[letter] += 1

    # Divide double letters by two
    balloon['L'] = balloon['L'] // 2
    balloon['O'] = balloon['O'] // 2

    # return minimum frequency
    return min(balloon.values())


if __name__ == '__main__':
    print(solution('BALLOON'))
    print(solution('BAONXXOLL'))
    print(solution('BAOOLLNBALLOONBALLOONBALLOON'))
    print(solution('BALLON'))
