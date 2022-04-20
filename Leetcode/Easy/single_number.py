def singleNumber(nums):
	l = []
	for i in nums:
		if i not in l:
			l.append(i)
		elif i in l:
			l.remove(i)
		
	return l[0]

singleNumber([2,2,1])