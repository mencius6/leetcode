def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(k):
        nums[:] = nums[-1:] + nums[0:len(nums) - 1]


def rotate1(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    length = len(nums)
    nums[:] = nums[length - k:] + nums[:length - k]



nums = [1, 2]
rotate1(nums, 3)
print(nums)
