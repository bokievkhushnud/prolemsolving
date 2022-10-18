nums = [1,3,5,6]
target = 5
def searchInsert(nums, target):
    for i in nums:
        if i == target:
            return nums.index(i)
        if i < target:
            continue
        elif i>target:
            return nums.index(i)-1
        
print(searchInsert(nums, target))