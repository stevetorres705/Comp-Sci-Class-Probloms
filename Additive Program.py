# ADDITIVE PROGRAM 
'''
PROBLEM: 

Write a Python program that sums the integer numbers starting at 1 until x, where x will be a prompt to the user. 
For example, if the user enters 3 the answer should be 6 based on the logic (1+2+3=6). 
If the user enters 5, the answer should be 15 based on the logic (1+2+3+4+5=15). 
'''

# DAFT PUNK
def addem(n):
    global x
    x = 0
    global y
    y = 0
    while x != n:
        x+=1
        y = y + x
    return y

# MEAT

n = int(input("Enter the number you want to go to: "))
addem(n)
print("The sum of", n,"consecutive numbers starting at 1 is", y)

