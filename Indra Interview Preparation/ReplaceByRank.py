n = int(input("Enter the number of elements\n"))
array = list(map(int, input("Enter the numbers:").strip().split()))[:n]
sortedArray = sorted(array)

newArray = []
memo = {}

for i in range(0, len(sortedArray)):
    memo[sortedArray[i]] = i

for k, v in memo.items():
    newArray.insert(v, array.index(k)+1)

print(newArray)
