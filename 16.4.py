
test_list = [(3, 4), (6, 5), (7, 8)]


print("The original list is : " + str(test_list))


res = [(sub[1], sub[0]) for sub in test_list]
		

print("The swapped tuple list is : " + str(res))
