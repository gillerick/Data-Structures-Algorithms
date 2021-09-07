def findDuplicate(nums):
    # Let tortoise and hare start at the head
    tortoise = hare = nums[0]
    while True:
        # Move the tortoise in linear speed and the hare in double speed
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    ptr1 = nums[0]
    ptr2 = tortoise
    if ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    return ptr2


print(findDuplicate([1, 2, 2, 4, 6, 7]))
