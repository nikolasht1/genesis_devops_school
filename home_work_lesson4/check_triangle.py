     
# function to check if three sides
def checkSides(a, b, c):
    if (a+b < c) or (a+c < b) or (b+c < a):
        print("Invalid value for triangle!")
        return
    if (a == b == c):
        print("The triangle is equilateral.")
        return
    elif (b == a) or (c == b) or (a == c):
        print("The triangle is isosceles.")
               
    elif (a*a+b*b == c*c) or (a*a + c*c == b*b) or (b*b+c*c == a*a):
        print ("The triangle is rectangular.")
    else:
        print ("The triangle is versatile.")

try:
    a = float (input ("Please enter a value side, a: "))
    b = float (input ("Please enter a value side, b: "))
    c = float (input ("Please enter a value side, c: "))
 
    checkSides(a, b, c)
except:
    print("Oops! Invalid value... ")
