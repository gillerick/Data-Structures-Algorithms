"""
Game Rules:
Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring:
A player gets +1 point for each occurrence of the substring in the string .

"""


def minion_game(string):
    if staurt(string) > kevin(string):
        print(f"Staurt {staurt(string)}")
    else:
        print(f"Kevin {kevin(string)}")


def staurt(s):
    score = 0
    for c in s:
        count = 0
        if c != "a" or c != "e" or c != "i" or c != "o" or c != "u":
            count += s.count(c, s.index(c), len(s))
            score += count
    return score


def kevin(s):
    score = 0
    for c in s:
        count = 0
        if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
            count += s.count(c, s.index(c), len(s))
            score += count
    return score


if __name__ == '__main__':
    s = input()
    minion_game(s)
