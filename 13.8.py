
test_list = [56, 72, 875, 9, 173]


print("The original list is : " + str(test_list))


K = 7

res=[]
for i in test_list:
	if(str(i).find(str(K))!=-1):
		res.append(i)

print("Elements with digit K : " + str(res))
