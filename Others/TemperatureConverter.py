# Python Temperature Converter Program

unit = input("Temp in (C or F): ")
temp = float(input("Enter temperature: "))

if unit == "C":
    result = round(((9 * temp)/5 + 32),3)
    print(f"The temperature in F is: {result}F")
elif unit == "F":
     result = round(((temp - 32)*5/9),3)
     print(f"The temperature in C is: {result}C")
else:
     print(f"{unit} is not valid")
