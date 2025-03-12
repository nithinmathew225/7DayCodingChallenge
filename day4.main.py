from typing import List


def largestAltitude(gain: List[int]) -> int:
    max_difference = 0
    current_difference = max_difference
    for g in gain:
        current_difference += g
        max_difference = max(max_difference, current_difference)
    print(max_difference)
    return max_difference


gain = [-5,1,5,0,-7]
largestAltitude(gain)