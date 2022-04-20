q = [1, 2, 5, 3, 7, 8, 6, 4]
def minimumBribes(q):

    moves = 0
    q =[i-1 for i in q]
    for i,j in enumerate(q):
        print(i,j)
        if j-i >2:
            print("Too chaotic")
            return
    
    print(moves)



# def minBar(q):
#     n = len(q)
#     while n>=1:
#         if q.index(n)
minimumBribes(q)
