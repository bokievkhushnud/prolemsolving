# Easy
a=[17, 28, 30]
b=[99, 16, 8]
def compareTriplets(a, b):
    alice=0
    bob=0
    for i in range(len(a)):
        if a[i]>b[i]:
            alice+=1
        elif a[i]<b[i]:
            bob+=1
        else:
            continue
    return [alice,bob]
print(compareTriplets(a,b))



