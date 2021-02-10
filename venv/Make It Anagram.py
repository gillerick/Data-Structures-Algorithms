"""
Problem Statement:
Alice recently started learning about cryptography and found that anagrams are very useful. Two strings are anagrams of each other if they have the same character set.
e.g. strings "dcbac" and "bacdc" are anagrams.

Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make two strings anagrams.

Given two strings of different or same length, help her in finding out the minimum number of charcter delations required to make two strings anagrams. Any characters can be deleted from
te strings.

Input:
Two lines each containing a string

"""

class Solution(object):
    def solve_MLE(self, cipher):
        a, b = cipher
        a, b = list(a), list(b)
        m = len(a)
        n = len(b)
        a.sort()
        b.sort()

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m+1): dp[i][0] = i
        for j in range(n+1): dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if a[i-1] == b[j-1]: dp[i][j] = dp[i-1][j-1]
                else: dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        return dp[-1][-1]