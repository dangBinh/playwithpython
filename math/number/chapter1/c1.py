# factor are numbers we can mutiply together to get another number
# % operator is modulo
def is_factor(a, b):
	if b % a == 0:
		return True
	else:
		return False

print is_factor(3, 0)