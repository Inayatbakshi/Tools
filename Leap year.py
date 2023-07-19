year = int(input("enter the year you want to check: "))
if year % 4 == 0 and year % 100 != 0:
    print("it is a leap year")
elif year % 100 == 0 and year % 400 == 0:
    print("it is a leap year")
else:
   print("it is not leap year")