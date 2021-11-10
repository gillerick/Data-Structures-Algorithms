def repeated_string(s, n:int):
    occurrences_in_sub = list(s).count("a")
    substring_length = len(s)
    a, b = divmod(n, substring_length)
    infinite_string = s * a + s[:b]
    infinite_string_length = len(infinite_string)
    times = infinite_string_length//substring_length
    rem_string = infinite_string[times*substring_length]
    total = list(rem_string).count("a") + times*occurrences_in_sub
    return total


if __name__ == "__main__":
    print(repeated_string('aba', 10))
    print(10//3*"aba")
