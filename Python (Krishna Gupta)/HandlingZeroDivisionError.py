try:
    a = int(input("Enter Numerator:"))
    b = int(input("Enter Denominator:"))
    print("Result:", a/b)
except ZeroDivisionError:
    print("Error: Cannot Divide by Zero!")
except ValueError:
    print("Error: Please Enter Valid Numbers!")
    