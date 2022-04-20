 def isPalindrome(x):
        if x<0:
            return False
        return x == int(str(x)[::-1])
      
isPalindrome(121)
