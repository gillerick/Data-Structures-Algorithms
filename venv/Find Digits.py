"""
Problem Statement
You are given a number N, you need to print the number of positions where digits exactly divide N

Input Format
The first line contains T (number of test cases followed by T lines each containing N)
"""

class Solution(object):
    def solve(self, cipher):
        """main solution function
        :param cipher: the cipher
        """

        num = int(cipher)
        count = 0
        for char in cipher:
            digit = int(char)
            if digit == 0: continue
            if num % digit == 0: count += 1
        return count

if __name__ == "__main__":
    import sys

    f = open("Digits", "r")
    # f = sys.stdin
    testcases = 3

    for t in range(testcases):
        cipher = list(map(int, input("Enter the cipher").split()))
        print(cipher[0])
        s = f"{Solution().solve(cipher)}"
        print(s)
