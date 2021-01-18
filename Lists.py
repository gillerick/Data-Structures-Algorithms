"""
list.append(x) == a[len(a):] = [x]
list.extend(iterable) =  a[len(a):] = iterable
list.insert(i, x) i is the index of the element before which to insert the new element
list.remove(x) This removes the first item from the list whose value is equal to x
list.pop([i]) This removes the first item from the list whose value is equal to x and returns it
list.clear() = del a[:]
list.index(x[,start[,end]])
"""
a = [5]
a.append(6)
a[len(a):] = [8, 9, 8]
# print(len(a))
print(a.index(8, 3))

