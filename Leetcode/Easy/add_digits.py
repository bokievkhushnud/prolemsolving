num = 38
def adddigit(num):
	while (sum([int(i) for i in str(num)]))!=2:
		if num == 0:
			return 0
		if len(str(num))==1:
			return num
		num = (sum([int(i) for i in str(num)]))
	return(sum([int(i) for i in str(num)]))

print(adddigit(num))