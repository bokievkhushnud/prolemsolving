s=7
t=11
a=5
b=15
apples=[-2,2,1]
oranges=[5,-6]
def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apples=0
    count_oranges=0
    for i in apples:
        if (i+a)>=s and (i+a)<=t:
            count_apples+=1
    for j in oranges:
        if (j+b)<=t and (j+b)>=s:
            count_oranges+=1
    return count_apples, count_oranges
print(countApplesAndOranges(s,t,a,b,apples,oranges))