"""
Alex works at a clothing store. There is a large pile of socks that must be paired by color for sale.
Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are  socks with colors . There is one pair of color  and one of color .
There are three odd socks left, one of each color. The number of pairs is .

# """
n = int(input())
temp = input().split()
graph = {}
# Initialize the graph item
for item in temp:
    graph[item] = 0
# Update graph for items occurring more than once
for item in temp:
    graph[item] += 1
count = 0
for item in graph:
    count += int(graph[item]/2)
print(count)



