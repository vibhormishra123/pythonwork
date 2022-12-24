# code to print first 5 binary number using builtIn library


def Print_Binary_Number(num):
	for i in range(1, num+1):

		# using bin to print binary value
		print(int(bin(i).split('0b')[1]), end=" ")


# driver code
if __name__ == "__main__":
	num = 5
	Print_Binary_Number(num)
