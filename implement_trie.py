# LeetCode 208


# node class
class Node:
    def __init__(self):
        # key=letter value=node
        self.children = {}
        self.endOfWord = False

class Trie:

    # initialize tree
    def __init__(self):
        self.root = Node()

    # Time Complexity: O(n)
    def insert(self, word: str) -> None:
        
        # set current node to root
        currNode = self.root
        
        # loop through letters of the word
        for i in word:
            # if the current letter is not in childrens hashmap, add it
            # key=letter value=node
            if i not in currNode.children:
                currNode.children[i] = Node()
            # move to the next node
            currNode = currNode.children[i]
            
        # flag the last letter of the word
        currNode.endOfWord = True
    
    # Time Complexity: O(n)       
    def search(self, word: str) -> bool:
        
        # start at root node
        currNode = self.root
        
        # loop through letters of word
        for i in word:
            # move to the next letter node if it exists
            if i in currNode.children:
                currNode = currNode.children[i]
            # if letter doesn't exist, word is not in trie
            else:
                return False
        
        # if the last node is the end of the word, return true
        if currNode.endOfWord:
            return True
        else:
            return False

    # Time Complexity: O(n)   
    def startsWith(self, prefix: str) -> bool:
        
        # start at root node
        currNode = self.root
        
        # loop through prefix letters
        for i in prefix:
            # is the letter exists in the trie, move to the next node
            if i in currNode.children:
                currNode = currNode.children[i]
            else:
                return False
        
        # if it gets here, the prefix is in the trie
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)