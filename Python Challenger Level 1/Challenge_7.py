try:

    total = 0

    while total <50:
        number = int(input("Add a number: "))
        total += number
        print(f"The total is {total}")

except Exception as e:
    print(f"Error: {e}")