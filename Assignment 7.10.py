s1=input("What is your favourite colour: ")
l1=["yellow","blue","orange","white","black","red"]
for colour in l1:
    if colour in s1:
        c = colour
        break
else:
    c = "other"
match c:
    case "yellow":
        print("Monday")
    case "blue":
        print("Monday")
    case "orange":
        print("Monday")
    case "white":
        print("Monday")
    case "black":
        print("Monday")
    case "red":
        print("Monday")
    case "other":
        print("Monday")

print()        
