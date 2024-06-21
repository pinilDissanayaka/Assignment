class Calculator:
    def __init__(self):
        pass
    
    def add(self, a:int, b:int)->int:
        print(f"The sum of {a} and {b} is {a+b}")
        return a + b

def main():
    calc = Calculator()
    result = calc.add(10, 12)
    
    
if __name__=="__main__":
    main()