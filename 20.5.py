num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

smallest = num1
if (num2 < num1) and (num2 < num3):
    smallest = num2
elif (num3 < num1):
    smallest = num3

print("The smallest number is", smallest)
