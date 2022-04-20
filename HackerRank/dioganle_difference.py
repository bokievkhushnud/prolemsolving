arr=[
[11, 2, 4],
[4, 5, 6],
[10, 8, -12]]

def diagonalDifference(arr):
    sum1=0
    sum2=0
    for i in range(len(arr)):
        sum1+=arr[i][i]
        sum2+=arr[i][len(arr)-i-1]
    return abs(sum1-sum2)

diagonalDifference(arr)