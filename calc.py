def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b
def pow(a,b):
    return a**b

if __name__ == "__main__":
    print("#Example of the calculator")
    print("2 + 3 =", add(2,3))
    print("5 - 2 =", sub(5,2))
    print("3 * 4 =", mul(3,4))
    print("8 / 2 =", div(8,2))
    print("9 ^ 3 =", pow(9,3))

print("for performing calculations kindly enter the number of the function")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponentiation")
print("6. Exit")

choice=input("Enter choice(1/2/3/4/5/6): ")
while choice in ['1','2','3','4','5']:
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    if choice=='1':
        print(num1,"+",num2,"=",add(num1,num2))
    elif choice=='2':
        print(num1,"-",num2,"=",sub(num1,num2))
    elif choice=='3':
        print(num1,"*",num2,"=",mul(num1,num2))
    elif choice=='4':
        try:
            print(num1,"/",num2,"=",div(num1,num2))
        except ValueError as e:
            print(e)
    elif choice=='5':
        print(num1,"^",num2,"=",pow(num1,num2))
    choice=input("Enter choice(1/2/3/4/5/6): ")
if choice=='6':
    print("Exiting the calculator. Goodbye!")
    break