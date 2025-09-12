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
    print("2 + 3 =", add(2,3))
    print("5 - 2 =", sub(5,2))
    print("3 * 4 =", mul(3,4))
    print("8 / 2 =", div(8,2))
    print("9 ^ 3 =", pow(9,3))
