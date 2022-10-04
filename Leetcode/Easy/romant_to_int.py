num = "MCMXCIV" 
# num = "III"
def romanToInt(s):
    dict_with_meanings = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            }
    result = 0
    i = 0
    while i<len(s):
        try:
            if (dict_with_meanings[s[i]]<dict_with_meanings[s[i+1]]):
                result+= dict_with_meanings[s[i+1]]-dict_with_meanings[s
                [i]]
                i+=2

            else:
                result+= dict_with_meanings[s[i]]
                
                i+=1
        except Exception as e:
            result+= dict_with_meanings[s[i]]
            
            break
        print(result)
    return result
    
print(romanToInt(num))