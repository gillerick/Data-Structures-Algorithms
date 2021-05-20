s = input("Enter String\n")
for char in s:
    if char in ' ':
        s = s.replace(char, '')
print(s)
