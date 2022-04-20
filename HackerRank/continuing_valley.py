path='UDDDUDUU'
for i in path:
    print(i)
def countingValleys(path):
    num=0
    val=0
    for i in path:
        if i=='U':
            val=val+1
            if val==0:
                num=num+1
        elif i=='D':
            val=val-1
    return num
countingValleys(path)
