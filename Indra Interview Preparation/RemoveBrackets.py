s = input("Enter string\n")
pattern = '()'
for char in s:
    if char in pattern:
        s = s.replace(char, '')
print(s)
