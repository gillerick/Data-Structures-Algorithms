class Solution(object):
    def solve(self, cipher):
        """main solution function
        :param cipher: the cipher"""

        A = cipher
        bit = 0
        for item in A:
            bit ^= item
        return bit