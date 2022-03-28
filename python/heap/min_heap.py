class MinHeap:
	def __init__(self, lst):
		self.list = self.build(lst)

	def build(self, lst):
		if not lst: return lst
		size = len(lst)
		i = (size // 2) - 1

		while i >= 0:
			self.shift_down(i, lst)
			i -= 1
		return lst

	def insert(self, val):
		self.list.append(val)
		self.shift_up(len(self.list)-1)
		return val

	def remove(self, index):
		if index >= len(self.list): return
		last_index = len(self.list)-1
		self.swap(self.list, index, last_index)
		del self.list[last_index]
		self.shift_down(index, self.list)
		return self.list[index]
	
	def shift_up(self, index):
		child = index
		parent = (child-1) // 2
		while parent >= 0 and child >= 0 and self.list[child] < self.list[parent]:
			self.swap(self.list, parent, child)
			child = parent
			parent = (child-1) // 2

	def shift_down(self, index, lst):
		parent = index
		size = len(lst)
		while parent < size:
			child1 = 2*parent + 1
			child2 = child1 + 1
			min_child = size+1
			if child1 < size: min_child = child1
			if min_child >= size or (child2 < size and lst[child2] < lst[child1]): min_child = child2
			if min_child >= size: break
			if lst[parent] > lst[min_child]:
				self.swap(lst, parent, min_child)
			else:
				break
			parent = min_child
		return lst

	def swap(self, a,i,j):
		a[i], a[j] = a[j], a[i]
