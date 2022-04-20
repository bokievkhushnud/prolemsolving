n=6
def staircase(n):
    a=' '
    b='#'
    ar=[((n-i)*a + i*b) for i in range(1,n+1)]
    for i in ar:
        print(i)
staircase(n)
