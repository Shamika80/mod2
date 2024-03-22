num1 = int(input("3"))
num2 = int(input("3"))
num3 = int(input("4"))

largest = num1
smallest = num1
equal_count = 0

if num2 > largest:
  largest = num2
elif num2 < smallest:
  smallest = num2
  equal_count += 1  

if num3 > largest:
  largest = num3
elif num3 < smallest:
  smallest = num3
  equal_count += 1 

if num1 == num2 == num3:
  print("All numbers are equal.")
else:
  print("The smallest number is:", smallest)
  print("The largest number is:", largest)
  if equal_count > 0:
    print(f"There are {equal_count} numbers equal to each other.")