def ADD(a, b):
    return a + b


def SUB(a, b):
    return a - b


def SQUARE(a):
    return a ** 2


def CUBE(a):
    return a ** 3


def main():
    num1 = float(input("\nEnter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, SQUARE(2), CUBE(3)): ")

    if operator == "+":
        result = ADD(num1, num2)
        print(f"Result of ADD({num1}, {num2}) = {result}")
    elif operator == "-":
        result = SUB(num1, num2)
        print(f"Result of SUB({num1}, {num2}) = {result}")
    elif operator == "2":
        result = SQUARE(num1)
        print(f"Result of SQUARE({num1}) = {result}")
    elif operator == "3":
        result = CUBE(num1)
        print(f"Result of CUBE({num1}) = {result}")
    else:
        print("Invalid operator! Please enter +, -, 2, or 3.")

if __name__ == "__main__":
    main()
