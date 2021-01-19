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

st = input()
vowels = ["A", "E", "I", "O", "U"]
scores = [0, 0]
l = len(st)
for i in range(0, l):
    words = l - i
    if st[i] in vowels:
        scores[1] += words
    else:
        scores[0] += words
if scores[0] > scores[1]:
    print("Stuart", scores[0])
elif scores[0] < scores[1]:
    print("Kevin", scores[1])
else:
    print("Draw")
