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
    command = list(input().split())

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
    elif "remove" in c:
        A.remove(c[1])


"""
Alternative solution:
L = []
N = int(input())
while 1:
    try:
        inp = raw_input().strip()
        while "  " in inp: inp.replace("  "," ")
        command = map(str,inp.split())
    except:
        break
    if len(command)>1: command[1]=int(command[1])
    if len(command)>2: command[2]=int(command[2])
        
    if command[0]=="sort":
        L.sort()
    elif command[0]=="print":
        print L
    elif command[0]=="reverse":
        #L.reverse()
        L=L
    elif command[0]=="pop":
        L.pop()
    elif command[0]=="insert":
        L.insert(command[1],command[2])
    elif command[0]=="append":
        L.append(command[1])
    elif command[0]=="remove":
        L.remove(command[1])

"""
