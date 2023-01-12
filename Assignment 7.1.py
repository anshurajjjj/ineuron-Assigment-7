#Write a python script to display the number of days in a given month number.
month_name = input("Input the name of Month: ")
if month_name == "February":
	print("No. of days: 28/29 days")
if month_name in ("April", "June", "September", "November"):
	print("No. of days: 30 days")
if month_name in ("January", "March", "May", "July", "August", "October", "December"):
	print("No. of days: 31 day")
