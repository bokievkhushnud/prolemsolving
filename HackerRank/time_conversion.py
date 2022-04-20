s="06:40:03AM"
# s=[i for i in s]
# print(s)
def timeConversion(s):
    new_s=""
    if s[-2]=='A' and s[0:2]=="12":
        new_s+='00'
        new_s+=s[2:8]
    elif s[-2]=='A' and s[0:2]!="12":
        new_s+=s[0:8]
    elif s[-2]=='P' and s[0:2]=="12":
        new_s+=s[0:8]
    else:
        h=int(s[0:2])+12
        new_s+=str(h)
        new_s+=s[2:8]
    return new_s
print(timeConversion(s))