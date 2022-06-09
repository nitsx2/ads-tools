from tree_node import TreeNode
from pprint import pprint
class Bst:

	def __init__(self):
		self.root = None



	def search(val):


		root = self.root
		if not root: return None

		def searchhelper(root, val):
			if root.val == val:
				return root
			elif val < root.val:
				searchhelper(root.left, val)
			else:
				searchhelper(root.right, val)

		return searchhelper(root, val)





		'''
	clone insertion- if we are on correct parent's left or right, then we will insert node here , thats why we are returning the node.on recursion backtime it will get inserted at the left or right side of its actual parent.
	otherwise we go left or right based on condition and when we are coming back from recrusion after adding the node to its correct position, we will do-

	root.left = left_subtree 
	root.right = right_subtree

	this condition will just override things.
	root,left = leftsubtree is already is on its correct position, we are just doing it again to escape from any damage when we are coming back from recursion.

	'''

	def insert(self, val):


		node = TreeNode(val)

		def insert_helper(root, node):
			if not root:
				return node
			
			if node.val < root.val:
				root.left = insert_helper(root.left, node)
			else:
				root.right = insert_helper(root.right, node)

			return root

		root = self.root
		
		if not root: 
			self.root = node
		else:			
			insert_helper(self.root, node)

		return



	def delete(self, val):

		def deletehelper(root, val):
			if not root:
				return root
			
			if val < root.val:
				root.left = deletehelper(root.left, val)
			elif val > root.val:
				root.right = deletehelper(root.right, val)
			else:
				if not root.right:
					return root.left
				if not root.left:
					return root.right
				
				temp = root.right
				mini = temp.val
				while temp.left:
					temp = temp.left
					mini = temp.val


				root.val = mini

				root.right = deletehelper(root.right, root.val)
			return root





		self.root = deletehelper(self.root, val)
		return self.root

	def inorder(self):

		def inorderhelper(node):
			if not node: return
			inorderhelper(node.left)
			res.append(node.val)
			inorderhelper(node.right)
		res = []
		inorderhelper(self.root)
		return res


bst = Bst()
bst.insert(5)
bst.insert(2)
bst.insert(91)
bst.insert(60)
bst.insert(50)
bst.insert(70)
bst.insert(101)
print(bst.inorder())
bst.delete(5)
print(bst.inorder())

