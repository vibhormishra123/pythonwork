# Python program to check if all
# ments in a List are same


def ckeckList(lst):

	ele = lst[0]
	chk = True

	
	for item in lst:
		if ele != item:
			chk = False
			break

	if (chk == True):
		print("Equal")
	else:
		print("Not equal")


#
lst = ['G', 'Ge', 'Gs', 'G', ]
ckeckList(lst)
