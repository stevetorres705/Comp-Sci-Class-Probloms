#MEAT


age = int(input("Enter An Age: "))

if age <= 1:
    print("You are an infant.")
elif age > 1 and age < 13:
    print("You are a child.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
elif age >= 20:
    print("You are an adult.")

