nums = [0,1,0,3,12]


def moveZeroes(nums):
	c = -1

	count = nums.count(0)
	i = 0
	while i<len(nums)-count:
		if nums[i]==0:
			for j in range(i,len(nums)-1):
				nums[j]=nums[j+1]
			nums[c]	= 0
			c=-1
		if nums[i]==0:
			continue
		else:
			i+=1


moveZeroes(nums)
print(nums)