weight = int(input("Weight: "))
unit = input("K(g) or L(bs): ")

if unit.lower() == "k":
    weight = weight * 2.2
    print("Your weight in L(bs) is "+str (weight))
elif unit.lower() == "l":
    weight = weight / 2.2
    print("Your weight in Kg is "+ str (weight))
else:
    print("Enter the correct unit and Try again ")
    
