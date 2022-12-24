class ks:
	course = 'DSA'

	def purchase(obj):
		print("Purchase course : ", obj.course)


ks.purchase = classmethod(eks.purchase)
ks.purchase()
