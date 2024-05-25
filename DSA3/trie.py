class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_complete = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node = node.children[char]
        node.is_complete = True
    
    def search(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_complete
    
    def starts_with(self,prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self,word):
        if not self.search(word):
            return

        node = self.root
        stack =[]

        for char in word:
            stack.append((node,char))
            node = node.children[char]
        node.is_complete = False
        for current,char in reversed(stack):
            if not current.children[char].children and not current.children[char].is_complete:
                del current.children[char]
            else:
                break

trie =Trie()
trie.insert('care')
trie.insert('carrier')
trie.insert('carrera')
trie.delete('care')

print(trie.search('care'))
            
    
    