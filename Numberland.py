from itertools import combinations

def combine(arr):
    return list(x for l in range(2, len(arr)+1) for x in combinations(arr, l))


count = 0
e, o = input().split()
even = []
odd = []
for i in range(2, int(e)*2+1, 2):
    even.append(i)

for j in range(1, int(o)*2+1, 2):
    odd.append(j)

for odd_num in odd:
    a = [x for x in even if x < odd_num]
    a.append(odd_num)
    combos = [x for x in combine(a) if odd_num in x]
    count += len(combos)

for even_num in even:
    a = [y for y in odd if y < even_num]
    a.append(even_num)
    combos = [x for x in combine(a) if even_num in x]
    count += len(combos)


print(count)




