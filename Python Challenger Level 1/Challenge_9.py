try:

    while True:
        year = int(input("Enter the number of years: "))

        if year == 1:

            print(f"In {year} year there are..\nTotal of {year*12} months, Total of {year*365} of days.")
        else:
            print(f"In {year} years there are..\nTotal of {year * 12} months, Total of {year * 365} of days.")

except Exception as e:
    print(f"Error: {e}")