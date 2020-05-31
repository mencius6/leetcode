def containsDuplicate(nums):
    nums = sorted(nums)
    result = False
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            result = True
            break
    return result


print(containsDuplicate([1, 2, 3, 1]))
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
print(containsDuplicate([1, 2, 3, 4]))
