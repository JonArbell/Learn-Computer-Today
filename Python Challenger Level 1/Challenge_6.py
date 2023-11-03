try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"The total is {num1+num2}")
except Exception:
    print("Invalid input. Numbers should not contain any characters.")