digits = [1, 2, 3]


def plusOne(digits):
	digit = int("".join([str(i) for i in digits]))+1
	
	return [ int(i) for i in list(str(digit))]



plusOne(digits)