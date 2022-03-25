def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
if __name__=="__main__":
    a = int(input("enter the num1: "))
    b = int(input("enter the num2: "))

    addition = add(a, b)
    print(addition)
    subtraction = sub(a, b)
    print(subtraction)
    multiplication = mul(a, b)
    print(multiplication)
    division = div(a, b)
    print(division)