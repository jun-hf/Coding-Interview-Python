"""

Given n distinct number in an array, find the missing number at you will get from 0 - n range, but inside the array you will get o - n -1 array.
find the 

[2,1,3]

i = 0 
n = 3 

nums[i] = nums[0] = 2
nums[j] = nums[2] = 3

j = 2

[3, 1, 2]

j = 3




"""

def find(nums):
    i, n = 0, len(nums)

    while i < n:
        j = nums[i]

        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for item in range(n):
        if item != nums[item]:
            return item

    return n
