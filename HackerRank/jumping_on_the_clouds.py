c=[0, 0, 0, 1, 0, 0]

def jumpingOnClouds(c):
    num=0
    i=0
    while i<(len(c)-1):
        try:
            if c[i+2]==0:
                i+=2
                num+=1
                continue
            elif c[i+1]==0:
                i+=1
                num+=1
        except IndexError:
            if c[i+1]==0:
                i+=1
                num+=1
    print(num)
jumpingOnClouds(c)