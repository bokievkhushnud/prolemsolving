nums = [1,1,1,2,2,3]
def removeDuplicates(nums):
	for i in nums:
		if nums.count(i)>2:
			nums.remove(i)
	for i in nums:
		if nums.count(i)>2:
			nums.remove(i)


removeDuplicates(nums)