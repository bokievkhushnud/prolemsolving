x1=43
v1=2
x2=70
v2=2
def kangaroo(x1, v1, x2, v2):
    x=0
    if (v1-v2)==0:
        return 'NO'
    else:
        x=(x2-x1)/(v1-v2)
        if x==int(x) and x>0:
            return 'YES'
        else:
            return 'NO'
print(kangaroo(x1,v1,x2,v2))