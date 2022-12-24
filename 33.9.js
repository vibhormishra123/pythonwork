# 
def printMultiples(n):

	#
	unit_digit = n % 10

	# if the unit digit is 0 then
	# change it to 10
	if (unit_digit == 0):
		unit_digit = 10

	for i in range(unit_digit, n + 1,
				unit_digit):
		print(i, end = " ")

# Driver Code
n = 39

printMultiples(n)


