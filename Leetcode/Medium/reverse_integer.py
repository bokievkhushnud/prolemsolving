
x = 1534236469
# x=123


def reverse(x):
	# num = 0
	if str(x)[0] == '-':
		x = int('-'+str(x)[1:][::-1])
	else:
		x = int(str(x)[::-1])

	if x<=(-2)**31 or x>=(2**31)-1:
		return 0
	else:
		return x
print(reverse(x))
