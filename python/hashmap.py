class Node:
	def __init__(self, key, val):
		self.key = key
		self.val = val
		self.next = None
		self.prev = None



class HashMap:
	def __init__(self, size=1024):
		self.size = size
		self.list = [Node(float('inf'), float('inf')) for i in range(size)]



	def get_index(self, key):
		return key % self.size


	def insert(self, key, val):
		index = self.get_index(key)
		head = self.list[index]
		node = self.get_node(key)
		
		if not node:
			return self.insert_in_list(head, Node(key, val))
		else:
			node.val = val

		return True

	def get(self, key):
		index = self.get_index(key)
		head = self.list[index]
		node = self.get_node(key)
		if not node:
			raise ValueError(f"KeyError {key}")
		return node.val

	def get_node(self, key):
		index = self.get_index(key)
		head = self.list[index]
		cur = head
		while cur:
			if cur.key == key: return cur
			cur = cur.next
		return None


	def delete(self, key):
		index = self.get_index(key)
		head = self.list[index]
		node = self.get_node(key)
		if not node: return False
		self.delete_in_list(node)
		return True


	def insert_in_list(self, head, node):
		prev = None
		cur = head

		while cur:
			prev = cur
			cur = cur.next

		prev.next, node.prev = node, prev
		return True


	def delete_in_list(self, node):
		prev, nxt = node.prev, node.next
		if prev and nxt:
			prev.next, nxt.prev = nxt, prev
		elif not nxt:
			prev.next = None


hash = HashMap()
hash.insert(1,"nitin")
hash.insert(2,"sharma")
print(hash.get(1))
hash.delete(1)
print(hash.get(1))
