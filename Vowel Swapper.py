store = {'a': 4, 'e': 3, 'i': '!', 'o': 'ooo', 'O': '000', 'u': '|_|'}


def vowel_swapper(string: str):
    string = change_to_lower(string)
    for vowel, replacement in store.items():
        string = string.replace(vowel, str(replacement))
    return string


def change_to_lower(string: str):
    for char in string:
        if char != 'O' and char in store.items():
            string = string.replace(char, char.lower())
    return string


if __name__ == "__main__":
    print(vowel_swapper('strOng\n'))
    print(vowel_swapper('aA eE iI oO u\n'))
    print(vowel_swapper('Hello World\n'))
    print(vowel_swapper('Everything\'s Available\n'))
