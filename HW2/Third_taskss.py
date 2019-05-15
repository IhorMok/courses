year = int(input("Enter the year: "))
if year % 4 != 0:
    print("Usual year")
elif year % 100 == 0:
    if year % 400 == 0:
        print("Intercalary year")
    else:
        print("Usual year")
else:
    print("Intercalary year")