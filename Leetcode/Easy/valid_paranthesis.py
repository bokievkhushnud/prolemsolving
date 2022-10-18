# s = "(]"
s = '()'

def isValid(s):
    if len(s)==1:
        return False
    stack_par = [0]
    for i in s:
        if i == ')' and stack_par[-1]=='(':
            del stack_par[-1]
        elif i == ']' and stack_par[-1]=='[':
            del stack_par[-1]
        elif i == '}' and stack_par[-1]=='{':
            del stack_par[-1]
        else:
            stack_par.append(i)
    if len(stack_par)==1 and stack_par[0]==0:
        return True
    else:
        return False

print(isValid(s))
