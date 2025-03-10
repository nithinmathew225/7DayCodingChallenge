from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    length = len(nums)
    for j in range(length):
        if nums[j] != 0:
            nums[i] = nums[j]
            if i != j:
                nums[j] = 0
            i += 1

nums = [0,0,1,0,1]
moveZeroes(nums)