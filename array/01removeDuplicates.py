def removeDuplicates(nums):
    #从数组最后一个元素开始比较，如果和前一个元素相同，就删除掉
    for i in reversed(range(len(nums))):
        #要考虑数组被删除只剩一个元素的情况
        if len(nums) == 1:
            return 1
        if nums[i] == nums[i - 1]:
            del nums[i]
    return len(nums)


nums = [1, 1]
print(removeDuplicates(nums))
