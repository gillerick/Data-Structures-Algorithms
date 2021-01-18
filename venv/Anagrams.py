"""Given two strings, check if they are anagrams.

e.g. Public Relations and Crap built on lies"""


def anagram(s1, s2):
    # Remove spaces and lowercase letters
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    return sorted(s1) == sorted(s2)


print(anagram("Gill", "ill "))
