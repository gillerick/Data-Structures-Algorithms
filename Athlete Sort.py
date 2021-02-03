"""
You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight and so on).
 You are required to sort the data based on the Kth attribute and print the final resulting table.
 Follow the example given below for better understanding.

"""

from typing import List

rows, columns = input().split()
record: List[List[int]] = []
temp = {}
for r in range(0, int(rows)):
    record.append(list(map(int, input().split())))
k = int(input())
for i in range(len(record)):
    temp[i] = record[i][k]

sorted_temp = dict(sorted(temp.items(), key=lambda item: item[1]))
for k, v in sorted_temp.items():
    # Print individual array elements
    print(*record[k])
