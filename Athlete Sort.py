rows, columns = input().split()
record = []
for r in range(0, int(rows)):
    record.append(list(map(int, input().split())))

print(record)
