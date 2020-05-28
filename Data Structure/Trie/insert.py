# maro babudo



class TrieNode:
	def __init__(self, val=None):
		self.val = val
		self.children = []
		for i in range(26):
			self.children.append(None)
			# self.children.append(TrieNode())
			 # ???????// is this ^^^ any error
		self.isend = False


class Trie:
	def __init__(self):
		# root will contain the list in which we will have 'a' to 'z'
		self.root = TrieNode()
		# we can later append character in root


	def insert(self, string:str):
		currentNode = self.root

		for i in string:
			index = ord(i) - ord('a')

			if currentNode.children[index] != None:
				currentNode = currentNode.children[index]
			else:
				currentNode.children[index] = TrieNode(i)
				currentNode = currentNode.children[index]
				print(currentNode.val)

		currentNode.isend = True

	def search(self, string:str):
		currentNode = self.root

		for i in string:
			index = ord(i) - ord('a')
			if currentNode.children[index] != None:
				currentNode = currentNode.children[index]
				
			else:
				return False


		if currentNode.isend == True:
			return True
		else:
			return False


oMNS = Trie()
oMNS.insert("omns")
oMNS.insert("omnsmaroshiv")
oMNS.insert('maroshiv')
oMNS.insert('mahakal')
print(oMNS.search("omns"))

