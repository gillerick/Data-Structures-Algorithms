def selectionssort(mylist):
    pos = -1
    if len(mylist) > 1:
        for i in range(len(mylist[:pos])):
            largest = max(mylist[:pos])
            print(largest)
            mylist[pos] = largest
            print(mylist[:pos])
            # print(mylist[:pos])
            pos += -1
        print(mylist)


arr = [2, 45, 6, 7, 1, 2, 56, 3, 5]
selectionssort(arr)
