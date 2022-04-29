from collections import Counter
# s = "leetcode"
s = "loveleetcode"
def firstUniqChar(s):
	sdic = Counter(s)    
	for i,c in enumerate(s):
		if sdic[c] == 1:
			return i
	return -1 

print(firstUniqChar(s))

