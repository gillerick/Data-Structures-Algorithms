s = list(map(str, input("Enter String").split(" ")))
for word in s:
    for i in range(len(word)):
        word[-1].upper()
        word[0].upper()

print(s)
