def compress(string):
    memo = {}
    compressedString = ""
    for char in string.lower():  # O(n)
        if char.lower() in memo:
            memo[char] += 1
        else:
            memo[char] = 1

    for k, v in memo.items():  # O(n)
        compressedString += str(k) + str(v)
    return compressedString


if __name__ == "__main__":
    print(compress("Aaabbcdeee"))
