def main():
    until=int(input("Enter integer Number : "))
    
    if type(until) is not int:
        raise Exception("Only integers are allowed")
    if until <0:
        raise Exception("Only positive integers are allowed")
    
    for i in range(0, until):
        number=getFibonacci(until=i)
        print(number, end=" ")


def getFibonacci(until:int)->int:    
    if (until <=1):
        return until
    else:
        return getFibonacci(until=(until-1)) + getFibonacci(until=(until-2))
        
        
    
if __name__=="__main__":
    main()