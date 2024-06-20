def main()->None:
    number = int(input("Enter positive integer :"))
    
    if type(number) is not int:
        raise Exception("Only integers are allowed")
    if number <0:
        raise Exception("Only positive integers are allowed")
    
    factorial=getFactorial(number=number)
    
    print(f"Factorial of {number} is {factorial}")

def getFactorial(number:int):
    if (number==0) or (number ==1):
        return 1
    else:
        return number * getFactorial(number=(number-1))
    
    
if __name__=="__main__":
    main()
        
    
