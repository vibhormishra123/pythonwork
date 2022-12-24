
import re


def remove(list):
	pattern = '[0-9]'
	list = [re.sub(pattern, '', i) for i in list]
	return list




list = ['4eggs', '3for', '4eggs']
print(remove(list))
