year = int(input("Enter a year: "))

# Check if the year is a leap year
# if a year is divisible by 4 is a leap year
# if year is divisible by 100 is not leap year until its is also divisible by 400
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("year is a leap year.")
else:
    print("year is not a leap year.")