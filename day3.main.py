from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
    window_sum = sum(nums[:k])
    max_value = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_value = max(max_value, window_sum)
    result = max_value / k
    print(result)
    return result
nums= [0,1,1,3,3]
findMaxAverage(nums,4)