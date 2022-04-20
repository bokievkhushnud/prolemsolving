s = "abcd"
t = "abcde"
def finddif(s,t):
	for i in t:
		if s.count(i)== t.count(i):
			continue
		if t.count(i)>s.count(i):
			return i

finddif(s,t)
