
def fizzBuzz(n):
    # Write your code here
    for i in range (n):
        num = i+1
        if(num%5==0 and num%3==0):
            print("FizzBuzz")
        elif(num%5==0 and num%3!=0):
            print("Buzz")
        elif(num%5!=0 and num%3==0):
            print("Fizz")
        else:
            print(num)

if __name__ == '__main__':
    fizzBuzz(int(input()))