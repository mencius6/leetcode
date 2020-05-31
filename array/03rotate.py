def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(k):
        nums[:] = nums[-1:] + nums[0:len(nums) - 1]


nums = [1,2]
rotate(nums, 3)
print(nums)
