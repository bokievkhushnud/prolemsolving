a=[3,4]
b=[24,48]
def check1(i,b):
    for j in b:
        if j%i==0:
            continue
        else:
            return 0
    return 1
def check2(i,a):
    for j in a:
        if i%j==0:
            continue
        else:
            return 0
    return 1
def getTotalX(a, b):
    count=0
    for i in range(a[-1],b[0]+1):
        if check2(i,a) and check1(i,b):
            count+=1
            print(i)
        else:
            continue
    return(count)
print(getTotalX(a,b))