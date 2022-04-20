import math
s="aba"
n=10
def repeatedString(s,n):
    num_a=0
    a_per_word=s.count('a')
    multiple=math.floor(n/len(s))
    num_a+=(a_per_word*multiple)

    multiple=n-(multiple*len(s))
    new_str=s*multiple
    new_str=new_str[0:multiple]
    num_a+=new_str.count('a')

    return num_a

print(repeatedString(s,n))