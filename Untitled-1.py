
def octal_in_range(n):

	
	for i in range(1, n+1):

		
		print(oct(i)[2:])


# Calling the function with input 3
print("Input: 3")
octal_in_range(3)

# Calling the function with input 11
print("Input: 11")
octal_in_range(11)
