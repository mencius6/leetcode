def maxProfit(nums):
    result = 0
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] > 0:
            result += nums[i] - nums[i - 1]
    return result


nums = [7, 1, 5, 3, 6, 4]
print(maxProfit([1, 2, 3, 4, 5]))
print(maxProfit([7, 6, 4, 3, 1]))
