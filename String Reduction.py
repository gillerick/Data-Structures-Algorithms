"""
Given a string, reduce it in such a way that all of its substrings are distinct. To do so, you may delete any characters
 at any index. What is the minimum number of deletions needed?

"""


def get_min_deletions(string):
    """Reasoning:
        Identify the redundant characters in the string parameter
        The number of deletions become the difference between the repeated characters and
        the initial string length
    """

    # A dictionary to store the unique characters in string parameter
    cache = {}
    for character in string:
        cache[character] = 1
    return len(string) - len(cache)


print(get_min_deletions('abcab'))  # Returns 2
print(get_min_deletions('abab'))  # Returns 2
print(get_min_deletions('aabcddde'))  # Returns 3
