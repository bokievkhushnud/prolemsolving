nums1 = [1,3]
nums2 = [2]
def median_of(nums1, nums2):
	new_arr = sorted(nums1+nums2)
	if len(new_arr)%2==0:
		i = int(len(new_arr)/2)
		med = (new_arr[i]+new_arr[i-1])/2
		return med
	else:
		return new_arr[int(len(new_arr)/2)]

print(median_of(nums1, nums2))
