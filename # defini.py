# defini
def evenOdd(n):
	
	#if remainder is 0 then num is even
	if(n % 2 == 0):
		return True
	
	#if remainder is 1 then num is odd
	elif(n %2 != 0):
		return False
	else:
		return evenOdd(n)


num = 3
if(evenOdd( num )):
	print(num ,"num is even")
else:
	print(num ,"num is odd")
