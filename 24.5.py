class G:
	domain = "g.org"


if __name__ == '__main__':
	g = k()
	print("Before deleting domain attribute from eks object:")
	print(gs.domain)
	delattr(eks, "domain")
	print("After deleting domain attribute from geeks object:")

	print(ks.domain)
