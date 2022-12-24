
def isDivisibleBy5(st) :
	n = len(st)
	return ( (st[n-1] == '0') or
		(st[n-1] == '5'))

# Driver code
st = "76955"
if isDivisibleBy5(st) :
	print ("Yes")
else :
	print ("No")
	

