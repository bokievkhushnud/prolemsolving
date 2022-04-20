nums1 = [4,9,5]
nums2 =[9,4,9,8,4]
def intersect(nums1, nums2):
	arr = []
	for i in nums1:
		if i in nums2:
			arr.append(i)
			nums2.remove(i)
	return arr
	
print(intersect(nums1, nums2))
