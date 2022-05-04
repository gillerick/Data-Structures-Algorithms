# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def twoSum(nums, target):
    nums_map = {}
    for index, number in enumerate(nums):
        summand_index = nums_map.get(target - number)
        if summand_index is not None and index != summand_index:
            return [index, summand_index]
        nums_map[number] = index


if __name__ == "__main__":
    nums = [2, 7, 8, 1]
    print(twoSum(nums, 3))
