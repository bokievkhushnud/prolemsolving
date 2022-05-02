nums = [3,1,2,4]

def sortArrayByParity(nums):
	even = [i for i in nums if i%2==0]
	odd = [i for i in nums if i%2!=0]

	return even+odd





sortArrayByParity(nums)

        