"""
Given an array with a range from 1 to n, no duplicate, sort it with o(N) with constant space

[2, 3, 1]

Design:

[2, 3, 1]

at the current pointer, get the value, minus one you will get the position the element should be: 2 -1 = 1, so 2 should be at index 1


"""

def cyclic_sort(nums):

    current_index = 0

    while current_index < len(nums):
        correct_index = nums[current_index] - 1

        if nums[correct_index] != nums[current_index]:
            nums[correct_index], nums[current_index] = nums[current_index], nums[correct_index]
        else:
            current_index += 1

    return nums


print(cyclic_sort([3, 2, 1, 4]))


