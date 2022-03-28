from tree_node import TreeNode
from ppretty import ppretty

class Bst:
	def __init__(self):
		self.root = None
		self.data = {}

	def insert(self, val):
		if not self.root:
			self.root = TreeNode(val)
			self.data[val] = self.root
		else:
			self.insert_helper(val, self.root)

	def insert_helper(self, val, cur_node):
		if not cur_node:
			cur_node = TreeNode(val)
			self.data[val] = cur_node
		elif val <= cur_node.val:
			cur_node.left = self.insert_helper(val, cur_node.left)
		else:
			cur_node.right = self.insert_helper(val, cur_node.right)
		return cur_node

	def delete(self, val):
		self.delete_helper(self.root, val)

	def delete_helper(self, root, val):
		if root is None: return root
		if val < root.val:
			root.left = self.delete_helper(root.left, val)
		elif val > root.val:
			root.right = self.delete_helper(root.right, val)
		else:
			if not root.left:
				return root.right
			if not root.right:
				return root.left
			
			node = self.find_right_min(root.right)
			root.val = node.val
			root.right = self.delete_helper(root.right, node.val)
		return root
	
	def find_right_min(self, root):
		while root.left is not None:
			root = root.left
		return root	
