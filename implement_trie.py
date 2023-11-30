class Trie:

    def __init__(self):
        self.root = self.TrieNode(isKey=False)

    def insert(self, word: str) -> None:
        pointer = self.root
        for i in range(1,len(word)+1):
            if word[:i] in pointer.children:
                pointer = pointer.children[word[:i]]
                if word == word[:i]:
                    pointer.isKey = True
            else:
                newChild = self.TrieNode(isKey=word==word[:i])
                pointer.children[word[:i]] = newChild
                pointer = newChild
        return None

    def search(self, word: str) -> bool:
        pointer = self.root
        for i in range(1,len(word)+1):
            if word[:i] in pointer.children:
                pointer = pointer.children[word[:i]]
            else:
                return False
        return pointer.isKey

    def startsWith(self, prefix: str) -> bool:
        pointer = self.root
        for i in range(1,len(prefix)+1):
            if prefix[:i] in pointer.children:
                pointer = pointer.children[prefix[:i]]
            else:
                return False
        return True
        
    class TrieNode:
        def __init__(self, isKey=False):
            self.isKey = isKey
            self.children = {}

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)