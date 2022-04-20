import math
n = int(input())
ar = list(map(int, input().rstrip().split()))
new_ar={
}
def make_dictionary(ar):
    for i in ar:
        if i not in new_ar:
            new_ar[i]=1
        elif i in new_ar:
            new_ar[i]+=1
    return new_ar
def sockMerchant(n, ar):
    make_dictionary(ar)
    num=0
    for i in new_ar.values():
        if i>1:
            n=math.floor(i/2)
            num+=n
            n=0
    return num
sockMerchant(n,ar)