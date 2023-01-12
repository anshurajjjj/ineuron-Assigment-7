#Write a python script to check whether a given year is
#a. Non century leap year
#b. Century leap year
#c. Non century non leap year
#d. Century non leap year
year = int(input("Enter a year: "))
if year % 400 == 0:
    print("{} is a century leap year")
if year % 100 == 0:
    print("{} is a century year")
if (year % 4 ==0) and (year % 100 != 0):
    print("{} is a non century leap year")
else:
    print("{} is a century non leap year")
