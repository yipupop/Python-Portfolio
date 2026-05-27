#coffee corrie

print("Welcome to Python Cafe!")
temp = input("Do you want a drink that is hot or cold? ")
if temp =="hot":
    flavor = input("Do you want a drink that is sweet or bitter? ")
    if flavor == "bitter":
        print("I recommend you should order a black coffee. ")
    if flavor =="sweet":
        print("I recommend you should order ahot chocolate. ")
if temp=="cold":
    flavor = input("Do you want a drink that is sweet or bitter? ")
    if flavor == "bitter":
        print("I recommend you should get a cold brew. ")
    if flavor =="sweet":
        print("I recommend you should get an iced latte. ")
