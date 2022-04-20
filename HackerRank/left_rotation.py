n=10
ar=[41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51]

# ar=[77 97 58 1 86 58 26 10 86 51 41 73 89 7 10 1 59 58 84 77]
def rotLeft(ar,n):
    new_dict=[i for i in range(len(ar))]
    diction={i:j for i,j in enumerate(ar)}
    for i in diction.keys():
        if i<n:
            l=len(ar)-(n-i)
            new_dict[l]=diction[i]
        else:
            l=i-n
            new_dict[l]=diction[i]
    return new_dict
print(rotLeft(ar,n))

