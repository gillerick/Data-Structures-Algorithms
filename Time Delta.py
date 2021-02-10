import re

s = "Fri 01 May 2015 13:54:36 -0000"
pattern1 = re.compile(r'[a-z]', re.IGNORECASE)
pattern2 = re.compile(r'[+\-\d*4]')


print(pattern1.findall(s))
print(pattern1.findall(s))

