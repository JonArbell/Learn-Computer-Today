try:

    while True:
        total = int(input("How much is the total bill? "))
        diners = int(input("How many diners are there? "))

        print(f"Each diner should pay ₱ {total / diners} each.\n")

except Exception as e:
    print(f"Error: {e}")