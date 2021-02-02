rows, columns = input().split()
record = []
temp = {}
for r in range(0, int(rows)):
    record.append(list(map(int, input().split())))
k = int(input())
for i in range(len(record)):
    temp[i] = record[i][k]

sorted_temp = dict(sorted(temp.items(), key=lambda item: item[1]))

print(record)
print(temp)
print(sorted_temp)
