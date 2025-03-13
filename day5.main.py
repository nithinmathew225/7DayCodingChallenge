from typing import List


def uniqueOccurrences( arr: List[int]) -> bool:
    result= {}
    for item in arr:
        if item in result.keys():
            result[item] = result[item] + 1
        else:
            result[item] =  1
    print(result)
    distint_value = list(result.values())
    return len(distint_value) == len(set(distint_value))

arr = [1,2,2,1,1,3]
result_value = uniqueOccurrences(arr)
print(result_value)