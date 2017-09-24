# coding: utf-8

def determinant(A):
	""" returns the determinant of square matrix A. """
	if len(A) > 2:
		det = 0
		for j, val in enumerate(A[0]):
			submatrix = list(map(lambda x: x[:j] + x[j + 1:], A[1:]))
			det += (-1) ** j * val * determinant(submatrix)
		return det
	elif len(A) == 2:
		# for 2x2 matrix
		return (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])
	else:
		# for 1x1 matrix
		return A[0][0]

if __name__ in "__main__":

	a = [[2, 3, 10], [2, 4, 10], [9, 6, 0]]
	print('A:')
	print(a)
	print('det(A):')
	print(determinant(a))
