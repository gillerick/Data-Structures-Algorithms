"""
You are given N words. Some words may repeat. For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word.
See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.

Constraints:
The sum of the lengths of all the words do not exceed 10^6
All the words are composed of lowercase English letters only.

Input Format:
The first line contains the integer, .
The next  lines each contain a word.

Output Format
Output  lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.
"""


def word_order():
    words = []
    temp = {}
    n = int(input())
    for i in range(n):
        words.append(input())
    for word in words:
        temp[word] = 0
    for word in words:
        temp[word] += 1

    unique_count = len(temp)
    print(unique_count)
    for v in temp.values():
        print(v, end=" ")


if __name__ == "__main__":
    print(word_order())
