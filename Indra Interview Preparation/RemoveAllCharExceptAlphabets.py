import re

s = input("Enter String\n")
pattern = re.compile('[^a-zA-Z]')
result = re.sub(pattern, "", s)
print(result)
