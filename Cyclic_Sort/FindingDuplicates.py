"""
You are unsorted given n+1 element range from 1..n, find the duplicates

Design:
[1,2,3,2]

def find_dup(nums):
    i = 0 

    while i < len(nums):
        j = nums[i] - 1

        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[i], nums[j]
        else:
            i += 1

    return nums[-1]

"""
nums = [1, 2, 2, 3]

i = 3

j = 2


def find_dup(nums):
    i = 0

    while i < len(nums):
        j = nums[i] - 1

        if nums[i] != nums[j]:  # nums[0] != nums[1], 2 != 1
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    return nums[-1]


print(find_dup([2, 1, 2, 3]))
