# Pascal's Triangle

triangle = []

for i in range(0, 11):
	newrow = []
	for j in range(0, i + 1):
		if j == 0 or j == i:
			newrow.append(1)
		else:
			newrow.append(triangle[-1][j] + triangle[-1][j - 1])

	triangle.append(newrow)

for row in triangle:
	print(row)