class Math:
	num = 87
	def __index__(self):
		return self.num
	def __int__(self):
		return self.num
obj = Math()
print(oct(obj))
