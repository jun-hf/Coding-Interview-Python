"""
[3,4,4,5,5]



"""
import math

def find_duplicates(nums):
    smallest_number = math.inf

    for i in range(len(nums)):
        smallest_number = min(smallest_number, nums[i])

    counter = 0 

    while counter < len(nums):
        j = nums[counter] - smallest_number

        if nums[j] != nums[counter]:
            nums[j], nums[counter] = nums[counter], nums[j]
        else:
            counter += 1


    duplicates = []

    for i in range(len(nums)):
        current_value = nums[i] - smallest_number

        if current_value != i:
            duplicates.append(nums[i])
    
    return duplicates



print(find_duplicates([3,4,4,5,5]))
print(find_duplicates([5,4,7,2,3,5,3]))