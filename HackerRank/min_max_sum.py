ar=[1, 2, 3, 4, 5]

def miniMaxSum(ar):
    a=ar.sort()
    min_sum=sum(ar[0:4])
    max_sum=sum(ar[1:])
    print(min_sum," ",max_sum) 
miniMaxSum(ar)
