# strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
def longestCommonPrefix(strs):
	pref = ""
	s = True
	c = 0
	try:
		while s:
			p = [i[c] for i in strs]
			if p.count(p[0])==len(p):
				pref+=p[0]
				c+=1
			else:
				s = False
	except IndexError as e:
		return pref
	return pref

print(longestCommonPrefix(strs))
