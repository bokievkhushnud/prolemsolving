import re
# s = "- 42,djkfhsd"
s = "   -42"
def myAtoi(s):
	s = s.strip()
	num = re.findall('[0-9-]', s)
	try:
		ind = s.index(' ')
	except ValueError as e:
		ind = len(s)+1
	if ind<	s.index(num[0]):
		return 0
	else:
		return int(''.join(num))
print(myAtoi(s))