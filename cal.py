def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    if y ==0:
        return "Error:Dvision by zero"
    return x / y
print("===Simple Calculator")
op =""
while op!="q":
    op=input("Enter operation(+,-,*,/ or q to quit):")
    if op=="q":
        print("\nExiting...goodbye!\n")
        break
    if op not in('+','-','*','/'):
        print("Invalid operator! Try again.\n")
        continue
    a=float(input("Enter first number:"))
    b=float(input("Enter second number:"))
    if op=='+':
        result=add(a,b)
    elif op=='-':
        result=subtract(a,b)
    elif op=='*':
        result=multiply(a,b)
    elif op=='/':
        result=division(a,b)
    print("Result:",result,"\n")
    
            