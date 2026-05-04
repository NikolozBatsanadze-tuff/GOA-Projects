num1 = int(input("Enter first number: "))
num2 = int(input("Enter your second number: "))


if num1 %2 == 0 and num2 %2 == 0:
    print("both numbers are even.")
elif num1 %2 != 0 and num2 %2 != 0:
    print("none are even")
elif num1 or num2 %2 == 0:
    print("only one is even")








