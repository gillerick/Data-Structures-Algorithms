"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the types
listed above. Iterate through each command in order and perform the corresponding operation on your list.

"""
# List to perform operations
A = []
# List to store commands
C = []
n = int(input())
for i in range(n):
    # try:
    command = input().split()

    C.append(command)
for c in C:
    # Check if the string command contains a substring
    if "insert" in c:
        A.insert(int(c[1]), c[2])
    elif "print" in c:
        print(A)
    elif "sort" in c:
        A.sort()
    elif "reverse" in c:
        A.reverse()
    elif "pop" in c:
        A.pop(int(c[1]))
    elif "append" in c:
        A.append(c[1])
