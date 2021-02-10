def reverse(s):
    length = len(s)
    i = 0
    spaces = [' ']
    words = []

    while i < length:
        if s[i] not in spaces:
            word_start = i

            while i < length and s[i] not in spaces:
                i += 1

            words.append(s[word_start:i])

        i += 1
    return "".join(reversed(s))


print(reverse(("This is a string")))