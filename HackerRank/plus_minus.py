n=6
arr=[-4, 3, -9, 0, 4, 1 ]

def plusMinus(arr):
    pos=0
    neg=0
    zer=0
    for i in arr:
        if i<0:
            neg+=1
        elif i>0:
            pos+=1
        else:
            zer+=1
    a=[pos,neg,zer]
    for j in a:
        print(format(j/n,'6f'))
plusMinus(arr)