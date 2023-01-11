"""
[2,2,1,4]

i = 0 
j = 3




"""

def find_missing_num(nums):
    i = 0 
    while i < len(nums):
        j = nums[i] - 1

        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    missing_num = []

    for i in range(len(nums)):
        if nums[i] != i + 1:
            missing_num.append(i+1)
            
    return missing_num

print(find_missing_num([2,2,1,4]))