class TreeNode:
	def __init__(self, val=None):
		self.val = val
		self.height = 1
		self.left = None 
		self.right = None 




class Bbst:

	def __init__(self):
		self.root = None

	
	def search(self, key):
		def searchhelper(node, key):
			if not node or node.val == key: return node

			if key < node.val:
				return searchhelper(node.left, key)
			else:
				return searchhelper(node.right, key)

		return searchhelper(self.root, key)


	def insert(self, key):
		def inserthelper(root, keynode):
			if not root: return keynode #we are on inserat-able position. return keynode so that it can be attached at reverse time of callstack 

			if keynode.val < root.val:
				root.left = inserthelper(root.left, keynode)
			else:
				root.right = inserthelper(root.right, keynode)

			self.update_height(root)
			return self.rotate(root)

		keynode  = TreeNode(key)
		self.root = inserthelper(self.root, keynode)
		return self.root


	def delete(self, key):
		def deletehelper(root, key):
			if not root: return None
			if key < root.val: #key will be deleted from left subtree
				root.left = deletehelper(root.left, key)
			elif key > root.val:
				root.right = deletehelper(root.right, key)
			else:
				# 4 cases
				if not root.left and not root.right: return None
				if not root.right: return root.left
				if not root.left: return root.right

				temp = root.right
				while temp.left:
					temp = temp.left

				tempval = temp.val
				temp.val = root.val
				root.val = tempval

				root.right = deletehelper(root.right, temp.val)
			
			self.update_height(root)
			return self.rotate(root)

		self.root = deletehelper(self.root, key)
		return self.root

	def rotate(self, node):
		
		def rotate_right(node):
			leftnode = node.left
			leftnoderight = leftnode.right
			leftnode.right = node
			node.left = leftnoderight
			self.update_height(node)
			self.update_height(leftnode)
			return leftnode


		def rotate_left(node):
			rightnode = node.right
			rightnodeleft = rightnode.left
			rightnode.left = node
			node.right = rightnodeleft
			self.update_height(node)
			self.update_height(rightnode)
			return rightnode

		balance_val = self.balance_val(node)
		if balance_val > 1: #left-heavy
			left_balance_val = self.balance_val(node.left)
			if left_balance_val < 0:
				node.left = rotate_left(node.left)
			return rotate_right(node)

		if balance_val < -1: #right-heavy
			right_balance_val = self.balance_val(node.right)
			if right_balance_val > 0:
				node.right = rotate_right(node.right)

			return rotate_left(node)

		return node


	def update_height(self, node):
		node.height = 1 + max(self.height(node.left), self.height(node.right))


	def height(self, node):
		if not node: return 0
		return node.height


	def balance_val(self, node):
		if not node: return 0
		return self.height(node.left) - self.height(node.right) 


	def inorder(self):
		def inorderhelper(node):
			if not node: return
			inorderhelper(node.left)
			res.append(node.val)
			inorderhelper(node.right)
		res = []
		inorderhelper(self.root)
		return res



bst = Bbst()
bst.insert(10)
bst.insert(20)
bst.insert(30)
bst.insert(15)
print(bst.inorder())
bst.delete(10)
print(bst.inorder())









































