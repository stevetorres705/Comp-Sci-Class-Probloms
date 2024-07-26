#MEAT
'''
Will tell you if, in the year you enter, feburary has 28 days or 29 
'''
year = int(input("Enter in a year and I'll tell you how many\ndays Febuary has in that year: "))


if (year%100) == 0:
    if (year%400) == 0:
        print("IN",year,"FEBRUARY HAD 29 DAYS.")
    else:
        print("IN",year,"FEBRUARY HAD 28 DAYS.")
elif (year%4) == 0:
    print("IN",year,"FEBRUARY HAD 29 DAYS.")
else:
    print("IN",year,"FEBRUARY HAD 28 DAYS.")
