import math

def mean(nums):
    return sum(nums) / len(nums)

def median(nums):
    # sort nums firstx
    nums.sort()
    size = len(nums)
    index = 0
    result = 0

    if size % 2 == 1:
        index = size / 2
        result =  nums[index]
    else:
        result += nums[int(math.ceil(size / 2))]
        result += nums[int(math.floor(size / 2))]
        result /= 2

    return result

nums = [0, 39, 2, 34, 129]
print(median(nums))
print(mean(nums))