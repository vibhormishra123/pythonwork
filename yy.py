# Python3 Program to find middle digit of number
import math

# Function to find the middle digit
def middleDigit(n):

	# Find total number of digits
	digits = math.log10(n) + 1;

	# Find middle digit
	n = int((n // math.pow(10, digits // 2))) % 10;

	# Return middle digit
	return n;

# Driver program

# Given Number N
N = 98562;

# Function call
print(middleDigit(N))
