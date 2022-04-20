def containsDuplicate(nums):
	if len(nums) == len(set(nums)):
		return False
	else:
		return True

containsDuplicate([1,2,3,1])