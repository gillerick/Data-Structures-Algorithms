"""

Given a string S
All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.

"""

import string

data = sorted(input())

lowercase = list(filter(lambda x: x in string.ascii_lowercase, data))
uppercase = list(filter(lambda x: x in string.ascii_uppercase, data))
digit = list(filter(lambda x: x in string.digits, data))

result = lowercase + uppercase + list(filter(lambda x: int(x) % 2 != 0, digit)) + list(filter(lambda x: int(x) % 2 == 0, digit))

print(*result, sep='')
