vowels = ['a', 'e', 'i', 'o', 'u', 'y']
total_grade = 0
n = input()
s = input().split()
for i in range(len(s)):
    count = 0
    for j in range(len(s[i])):
        if s[i][j] in vowels:
            count += 1
    if count % 2 == 0:
        total_grade += 2
    else:
        total_grade += 1
        continue
print(total_grade)
