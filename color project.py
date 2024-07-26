#MEAT

#color 1
color1 = input("Enter a primary color: ")
if (color1 == "red") or (color1 == "blue") or (color1 == "yellow"):
    print("Input is a primary color.")
    C1 = True
else:
    C1 = False
#color 2
color2 = input("Enter a second primary color: ")
if (color2 == "red") or (color2 == "blue") or (color2 == "yellow"):
    print("Second Input is a primary color.")
    C2 = True
else:
    C2 = False
    
#color mix
if (C1 and C2) == True:

    print("First color, (", color1, ") Second color, (", color2, ")")
    print("Mixing Colors..................")

    if (color1 == color2):
        print("The result is ", color1)

    elif (color1 == "red"):
        if (color2 == "blue"):
            print("Your color is purple.")
        elif (color2 == "yellow"):
            print("Your color is orange")

    elif (color1 == "blue"):
        if (color2 == "yellow"):
            print("Your color is green")
        elif (color2 == "red"):
            print("Your color is purple")
            
    elif (color1 == "yellow"):
        if (color2 == "blue"):
            print("Your color is green")
        elif (color2 == "red"):
            print("Your color is orange")
else:
    print("Err. One or both of the colors you entered are not primary colors.")




              
            
        
