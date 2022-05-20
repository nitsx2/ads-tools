
def bl_tr(a):
	rows,cols = len(a), len(a[0])

	for i in range(rows-1,-1,-1):
		for j in range(cols):
			print(a[i][j])


def topright_bottom_left(a):
	rows,cols = len(a), len(a[0])

	for i in range(rows):
		for j in range(cols-1,-1,-1):
			print(a[i][j])


def bottomr_topl(a):
	rows,cols = len(a), len(a[0])

	for i in range(rows-1,-1,-1):
		for j in range(cols-1,-1,-1):
			print(a[i][j])





def lowertringle_down_to_up(a):
	rows,cols = len(a), len(a[0])

	for i in range(rows-1,-1,-1):
		for j in range((rows-1) - i, cols):
			print(a[i][j])


def lowertringle_up_to_down(a):
	rows,cols = len(a), len(a[0])

	for i in range(rows):
		for j in range(cols-i-1, cols):
			print(a[i][j])



a = [[1,  2, 3, 4],
	 [5,  6, 7, 8],
	 [9, 10,11,12],
	 [14,15,16,17]
]

lowertringle_down_to_up(a)

print("===========================================")