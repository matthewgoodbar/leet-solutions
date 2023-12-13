class Trie:

    def __init__(self):
        self.root = self.TrieNode(val='', isKey=False)

    def insert(self, word: str) -> None:
        pointer = self.root
        for i in range(1,len(word)+1):
            if word[:i] in pointer.children:
                pointer = pointer.children[word[:i]]
                if word == word[:i]:
                    pointer.isKey = True
            else:
                newChild = self.TrieNode(val=word[:i], isKey=word==word[:i])
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
    
    def getPrefixNode(self, prefix: str):
        pointer = self.root
        for i in range(1,len(prefix)+1):
            if prefix[:i] in pointer.children:
                pointer = pointer.children[prefix[:i]]
            else:
                return None
        return pointer
    
    def getSuggestions(self, prefix: str) -> list[str]:
        prefixNode = self.getPrefixNode(prefix)
        if not prefixNode:
            return []
        else:
            return self.dfsSuggest(prefixNode, [])
    
    def dfsSuggest(self, node, suggestions) -> list[str]:
        if len(suggestions) == 3:
            return suggestions
        if node.isKey:
            suggestions.append(node.val)
            if len(suggestions) == 3:
                return suggestions
        for childKey in node.children:
            child = node.children[childKey]
            suggestions = self.dfsSuggest(child, suggestions)
            if len(suggestions) == 3:
                return suggestions
        return suggestions
                
        
    class TrieNode:
        def __init__(self, val, isKey=False):
            self.val = val
            self.isKey = isKey
            self.children = {}

class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        trie = Trie()
        products.sort()
        for product in products:
            trie.insert(product)
        res = []
        for i in range(1,len(searchWord)+1):
            res.append(trie.getSuggestions(searchWord[:i]))
            # suggs = trie.getSuggestions(searchWord[:i])
            # print(f'{searchWord[:i]}: {suggs}')
        return res

sol = Solution()
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
print(sol.suggestedProducts(products, searchWord))