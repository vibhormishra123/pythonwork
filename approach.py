# Python3 program for the above approach

def checkTriangle(x, y, z):

	
	if x == y == z:
		print("Equilateral Triangle")

	# Check for isosceles triangle
	elif x == y or y == z or z == x:
		print("Isosceles Triangle")
	
	else:
		print("Scalene Triangle")



x = 8
y = 7
z = 9

# Function Call
checkTriangle(x, y, z)
