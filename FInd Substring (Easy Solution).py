S = input()
ss = input()
count = 0
for i in range(0, len(S)):
    count += S.count(ss, i, i+len(ss))
print(count)
