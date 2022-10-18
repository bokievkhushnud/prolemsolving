import re
s = "   - 42,djkfhsd"
# s = "   -42"
s = "words and 987"
s = "3.14159"

def myAtoi(s):
	s = s.strip()
	num = re.findall('[0-9-]', s)

	try:
		ind = s.index(' ')
	except ValueError as e:
		ind = len(s)+1
	if ind < s.index(num[0]):
		return 0

	else:
		if '.' in num:
			num = num[:num.index('.')]
		if int(''.join(num))<-2147483648:
			return -2147483648
		elif int(''.join(num))>2147483647:
			return 2147483647
		else:
			return int(''.join(num))
print(myAtoi(s))