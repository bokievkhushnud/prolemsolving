from collections import Counter
s = "anagram"
t = "nagaram"

def isAnagram(s,t):
	s_col = Counter(s)
	t_col = Counter(t)
	if s_col == t_col:
		return True
	return False
print(isAnagram(s,t))

