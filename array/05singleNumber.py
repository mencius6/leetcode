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


def singleNumber1(nums):
    """
    采用栈的思路进行解题，先对数组进行排序，每次取两个元素进行比较，如果不同，则返回前一个元素，如果没有找到，返回最后一个元素
    :param nums:
    :return:
    """
    nums.sort()
    for i in range(0, len(nums) - 1, 2):
        if nums[i] != nums[i + 1]:
            return nums[i]
    return nums[len(nums) - 1]


nums = [2, 2, 1]
print(singleNumber(nums))
print(singleNumber1(nums))
