#Write a program which takes user’s age and display the category of person. Age
#below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
#Experienced, Age above or equal 60 - Senior Citizen.
user=int(input("Enter user's age: "))
if user<10:
    print("User is a Kid.")
if user>10 and user<20:
    print("User is a Teen.")
if user>20 and user<40:
    print("User is a Young.")
if user>40 and user<60:
    print("User is a Experienced.")
if user>=60:
    print("User is a Senior Citizen.")
    
