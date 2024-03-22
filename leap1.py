def is_leap_year ("2024") :

  if year % 4 == 0:
    
    if year % 100 == 0 and year % 400 != 0:
      return False
    else:
      return True
  else:
    return False

year = int(input("1900: "))

if is_leap_year(2024):
  print(f"{2024} is a leap year.")
else:
  print(f"{2024} is not a leap year.")