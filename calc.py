def add(numbers):
    return sum(numbers)

def sub(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def mul(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def div(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            raise ValueError("Division by zero")
        result /= num
    return result

def pow(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result **= num
    return result

def mod(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result %= num
    return result


if __name__ == "__main__":
    print("Welcome to the n-number calculator!")
    print("Choose the operation you want to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Modulus")
    print("7. Exit")

    while True:
        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice == '7':
            print("Exiting the calculator. Goodbye!")
            break

        n = int(input("Enter how many numbers you want to operate on: "))
        numbers = []
        for i in range(n):
            numbers.append(float(input(f"Enter number {i+1}: ")))

        try:
            if choice == '1':
                print("Result =", add(numbers))
            elif choice == '2':
                print("Result =", sub(numbers))
            elif choice == '3':
                print("Result =", mul(numbers))
            elif choice == '4':
                print("Result =", div(numbers))
            elif choice == '5':
                print("Result =", pow(numbers))
            elif choice == '6':
                print("Result =", mod(numbers))
            else:
                print("Invalid choice. Try again!")
        except ValueError as e:
            print(e,"Try again!,Can't divide by zero")
            


