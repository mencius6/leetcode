def singleNumber(nums):
    """
    采用栈的思路进行解题，先对数组进行排序，第一个元素先入栈，后续元素逐一比较，如果相同就出栈，否则入栈，最后剩余的一个元素就是唯一的元素
    :param nums:
    :return:
    """
    nums.sort()
    result = [nums[0]]
    for i in range(1, len(nums)):
        if len(result) != 0 and nums[i] == result[-1]:
            result.pop()
        else:
            result.append(nums[i])
    return result[0]


nums = [2, 2, 1]
print(singleNumber(nums))
