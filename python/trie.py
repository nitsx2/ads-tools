from ppretty import ppretty

class TrieNode:
	def __init__(self):
		self.childs = {}
		self.is_end = False
		self.counter = 0


class Trie:
	def __init__(self):
		self.root = TrieNode()



	def add_char(self, word):
		cur_node = self.root
		for char in word:
			if char in cur_node.childs:
				cur_node = cur_node.childs[char]
			else:
				cur_node.childs[char] = TrieNode()
				cur_node = cur_node.childs[char]

			cur_node.counter += 1
		cur_node.is_end = True


	def is_present(self, word):
		if not self.root: return False
		cur_node = self.root
		for char in word:
			if char not in cur_node.childs: return False
			cur_node = cur_node.childs[char]

		return cur_node.is_end



