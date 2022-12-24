


ini_tuple = (1, 2, 3, 4, 8, 12, 3, 34,
			67, 45, 1, 1, 43, 65, 9, 10)


print ("initial list", str(ini_tuple))
res = tuple(ini_tuple[x:x + 4]
	for x in range(0, len(ini_tuple), 4))


print ("resultant tuples", str(res))
