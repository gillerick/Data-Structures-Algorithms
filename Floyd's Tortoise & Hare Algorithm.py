def findDuplicate(nums):
    tortoise = hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 =nums[ptr1]
        ptr2 = nums[ptr2]
    return ptr2

print(findDuplicate([1, 2, 2, 4, 6, 7]))
