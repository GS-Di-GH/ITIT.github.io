import math
a = ""
def XandY():
	global X, Y
	X = float(input("Enter number X: "))
	Y = float(input("Enter number Y: "))
while a.lower() != "stop":
	XandY()
	print("X to the power of Y is equal to: " + str(int(X**Y)) + "\nThe logarithm of 2 from X is equal to: ",math.log2(X))
	a = input("If you done just print (stop), press (Enter) if not: ")