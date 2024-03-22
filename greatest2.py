num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

largest = num1
smallest = num1

if num2 > largest:
  largest = num2
elif num2 < smallest:
  smallest = num2

if num3 > largest:
  largest = num3
elif num3 < smallest:
  smallest = num3

print("The largest number is:", largest)
print("The smallest number is:", smallest)