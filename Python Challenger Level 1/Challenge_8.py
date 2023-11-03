try:

    while True:
        days = int(input("Enter the number of days: "))

        print(f"{days*24} total hours.\n{(days*24)*60} total minutes.\n{((days*24)*60)*60} total seconds.")

except Exception as e:
    print(f"Error: {e}")