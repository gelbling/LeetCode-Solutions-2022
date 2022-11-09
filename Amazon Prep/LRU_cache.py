# LeetCode 146

# Solution using hashmap and doubly linked list
# All operations are O(1)

class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next  = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}      # key=key value=node
        
        
        self.LRU = Node(0,0)
        self.MRU = Node(0,0)
        
        # initially pointing at eachother
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU

    def get(self, key: int) -> int:
        
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
            
        else:
            return -1
        
    def put(self, key: int, value: int):
                        
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            lru = self.LRU.next
            self.remove(lru)
            del self.cache[lru.key]
            
    # removes node from the linked list
    def remove(self, node):
        prev = node.prev
        nxt  = node.next
        prev.next = nxt
        nxt.prev  = prev
    
    # inserts into MRU's prev
    def insert(self, node):
        prev = self.MRU.prev
        prev.next = node
        node.prev = prev
        node.next = self.MRU
        self.MRU.prev = node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)