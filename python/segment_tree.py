


class SegmentTree:
	def __init__(self, arr):
		self.arr = arr
		self.n = len(arr)
		self.tree = [0]*(4*self.n)
		self.build(0, 0, self.n-1)


	def build(self, tree_index, start_index, end_index):

		if start_index == end_index:
			self.tree[tree_index] = self.arr[start_index]
			return self.tree[tree_index]

		mid = start_index + (end_index - start_index) // 2

		left_subtree_optimal_value = self.build(2*tree_index+1, start_index, mid)

		right_subtree_optimal_value = self.build(2*tree_index+2, mid+1, end_index)

		self.tree[tree_index] = min(left_subtree_optimal_value, right_subtree_optimal_value)
		return self.tree[tree_index]



	def update(self, index, new_val):

		def updatehelper(tree_index, node_contains_start, node_containes_end):
			nonlocal index, new_val

			if node_contains_start == node_containes_end:
				self.tree[tree_index] = new_val				
				return self.tree[tree_index]

			mid = node_contains_start + (node_containes_end - node_contains_start) // 2

			if index <= mid:
				updatehelper(2*tree_index+1, node_contains_start, mid)
			else:
				updatehelper(2*tree_index+2, mid+1, node_containes_end)



			self.tree[tree_index] = min(self.tree[2*tree_index+1], self.tree[2*tree_index+2])
			return self.tree[tree_index]


		self.arr[index] = new_val
		updatehelper(0, 0, self.n-1)
		return True



	def range(self, L, R):

		def rangehelper(tree_index, node_contains_start, node_containes_end):
			nonlocal L, R

			if R < node_contains_start or L > node_containes_end: return float('inf')

			if L <= node_contains_start and R >= node_containes_end: return self.tree[tree_index]

			mid = node_contains_start + (node_containes_end - node_contains_start) // 2

			left_res = rangehelper(2*tree_index+1, node_contains_start, mid)
			right_res = rangehelper(2*tree_index+2, mid+1, node_containes_end)

			return min(left_res, right_res)



		return rangehelper(0, 0, self.n-1)



a = [10,2,6,-3,5,8,1,15]

st  = SegmentTree(a)

print(st.tree)
# st.update(3, 5)
# print(st.tree)
print(st.range(0,3))
# print(rangequery(st, a, 1, 3))
# updatequery(st, a, 2, -50)
# print(rangequery(st, a, 7, 7))











# def build(a):

# 	def buildhelper(idx, node_start_index, node_end_index):
# 		nonlocal ST, a
# 		if node_start_index == node_end_index: #leaf node . just put the value of array
# 			ST[idx] = a[node_start_index]
# 			return
		
# 		mid  = (node_start_index + node_end_index) // 2

# 		lidx, ridx = 2*idx+1, 2*idx+2
# 		buildhelper(lidx, node_start_index, mid)
# 		buildhelper(ridx, mid+1, node_end_index)
# 		ST[idx] = min(ST[lidx], ST[ridx])


# 	N = len(a)
# 	ST = [0]*(4*N)
# 	buildhelper(0,0,N-1)
# 	return ST


# def rangequery(ST, a, L, R):
	
# 	def rangehelper(idx, node_start_index, node_end_index, L, R):
# 		nonlocal ST, IGNORE
# 		if L <= node_start_index and R >= node_end_index: return ST[idx]

# 		if node_start_index > R or node_end_index < L: return IGNORE

# 		mid = (node_start_index + node_end_index) // 2


# 		left_ans = rangehelper(2*idx+1, node_start_index, mid, L, R)
# 		right_ans = rangehelper(2*idx+2, mid+1, node_end_index, L, R)

# 		return min(left_ans, right_ans)

# 	IGNORE = float('inf')
# 	return rangehelper(0, 0, len(a)-1, L, R)




# def updatequery(ST, a, array_index, val):

# 	def updatehelper(idx, node_start_index, node_end_index):
# 		nonlocal ST, array_index, val
# 		if node_start_index == node_end_index:
# 			ST[idx] = val
# 			return

# 		mid  = (node_start_index+node_end_index) // 2

# 		lidx, ridx = 2*idx+1, 2*idx + 2

# 		if array_index <= mid:
# 			updatehelper(lidx, node_start_index, mid)
# 		else:
# 			updatehelper(ridx, mid+1, node_end_index)

# 		ST[idx] = min(ST[lidx], ST[ridx])

# 	updatehelper(0, 0, len(a)-1)













# a = [10,2,6,-3,5,8,1,15]
# st = build(a)

# print(rangequery(st, a, 1, 3))
# updatequery(st, a, 2, -50)
# print(rangequery(st, a, 7, 7))