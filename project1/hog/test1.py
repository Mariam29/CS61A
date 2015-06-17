def a(num):
	def b():
		return num + 1
	return b

t = a(4)

a = t()

print a