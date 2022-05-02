# s = "A man, a plan, a canal: Panama"
s = "0P1"
def isPalindrome(s):
	new_s = ""
	for i in s.lower():
		if i.isalpha() or i.isalnum():
			new_s+=i
		else:
			continue
	return new_s==new_s[::-1]

print(isPalindrome(s))
