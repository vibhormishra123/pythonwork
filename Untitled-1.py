
test_list = [4, 24, 8, 10, 12, 23]


print("The original list is : " + str(test_list))


div_list = [6, 4]


res = list(filter(lambda ele: all(ele % j == 0 for j in div_list), test_list))


print("All elements multiple of divisor list : " + str(res))
