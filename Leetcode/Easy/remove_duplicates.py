def removeDuplicates(nums):
    nums[:] = sorted(set(nums))
    return len(nums)

removeDuplicates([1,1,2])