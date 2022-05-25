						# idx = 0   1       2
# see tree like this => [[1,2,3], [2,3,4], [4,5,6]]
class SegmentTree:
	def __init__(self, matrix):
		self.rect  = matrix
		self.rows, self.cols = len(matrix), len(matrix[0])
		self.ini_seg = [[0 for _ in range(4*self.cols)] for _ in range(self.rows)]
		self.fin_seg = [[0 for _ in range(4*self.cols)] for _ in range(4*self.rows)]
		
		for tree_num in range(self.rows):
			self.build_ini_seg_tree(tree_num, 0, 0, self.cols-1)

		self.build_fin_seg_tree(0, 0, self.rows-1)

	def build_ini_seg_tree(self, tree_num, idx, start, end):

		if start == end:
			self.ini_seg[tree_num][idx] = rect[tree_num][end]
			return True
		
		mid = start + (end-start) // 2

		self.build_ini_seg_tree(tree_num, 2*idx+1, start, mid)
		self.build_ini_seg_tree(tree_num, 2*idx+2, mid+1, end)

		self.ini_seg[tree_num][idx] = self.ini_seg[tree_num][2*idx+1] + self.ini_seg[tree_num][2*idx+2]
		return True



	def build_fin_seg_tree(self, idx, start, end):
		if start == end:
			for i in range(4*self.cols):
				self.fin_seg[idx][i] = self.ini_seg[start][i]
			return True 

		mid = start + (end-start) // 2

		self.build_fin_seg_tree(2*idx+1, start, mid)
		self.build_fin_seg_tree(2*idx+2, mid+1, end)

		for i in range(4*self.cols):
			self.fin_seg[idx][i] = self.fin_seg[2*idx+1][i] + self.fin_seg[2*idx+2][i]

		return True


		# row trees finder
	def row_query(self, x1, y1, x2, y2, idx, node_start, node_end):
		

		if x2 < node_start or x1 > node_end :
			return 0

		if x1 <= node_start and x2 >= node_end:
			return self.col_query(idx, 0, 0, self.cols-1, y1, y2)

		mid = node_start + (node_end-node_start) // 2

		l = self.row_query(x1, y1,x2,y2, 2*idx+1, node_start, mid)
		r = self.row_query(x1,y1,x2,y2,2*idx+2, mid+1, node_end)
		return l+r


	def col_query(self, treeidx, idx, node_start, node_end, y1, y2):
		if y2 < node_start or y1 > node_end:
			return 0

		if y1 <= node_start and y2 >= node_end:
			return self.fin_seg[treeidx][idx]

		mid = node_start + (node_end-node_start) // 2

		l = self.col_query(treeidx, 2*idx+1, node_start, mid, y1, y2)
		r = self.col_query(treeidx, 2*idx+2, mid+1, node_end, y1, y2)
		return l+r

	#row tree finder
	def row_update(self, idx, node_start, node_end, row, col, val):
		if node_start == node_end:
			self.col_update(idx, 0, 0, self.cols-1, col, val)
			return True

		mid = node_start + (node_end-node_start) // 2

		if row <= mid:
			self.row_update(2*idx+1, node_start, mid, row, col, val)
		else:
			self.row_update(2*idx+2, mid+1, node_end, row, col, val)


		for i in range(4*self.cols):
			self.fin_seg[idx][i] = self.fin_seg[2*idx+1][i] + self.fin_seg[2*idx+2][i] 

		return True


	def col_update(self, treeidx, idx, node_start, node_end, index, val):
		if node_start == node_end:
			self.fin_seg[treeidx][idx] = val
			return True

		mid = node_start + (node_end-node_start) // 2

		if index <= mid:
			self.col_update(treeidx, 2*idx+1, node_start, mid, index, val)
		else:
			self.col_update(treeidx, 2*idx+2, mid+1, node_end, index, val)

		self.fin_seg[treeidx][idx] = self.fin_seg[treeidx][2*idx+1]	+ self.fin_seg[treeidx][2*idx+2]	
		return True




rect= [[ 1, 2, 3, 4 ],
	   [ 5, 6, 7, 8 ],
	   [ 1, 7, 5, 9 ],
	   [ 3, 0, 6, 2 ]]

s = SegmentTree(rect)
print(s.row_query(1, 1, 2, 2, 0, 0, len(rect)-1))
s.row_update(0, 0, len(rect)-1, 2,2,100)
# print(s.fin_seg)
print(s.row_query(1, 1, 2, 2, 0, 0, len(rect)-1))
