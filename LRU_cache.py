# INCOMPLETE
# half working...

class LRUCache:

    def __init__(self, capacity: int):
        self.recent = []
        self.data   = {}
        self.cap    = capacity
        

    def get(self, key: int) -> int:
        
        if key in self.data.keys():
            self.recent.remove(key)
            self.recent.insert(0,key)
            print(self.data[key])
            print('-------')
        else:
            print(-1)
            print('-------')

    def put(self, key: int, value: int):

        if key in self.recent and value not in self.data.values():
            self.data[key] = value
            print(self.recent, self.data)
            print('-------')
            return

        if key not in self.recent and value in self.data.values():
            self.recent.remove(value)
            self.recent.insert(0,key)
            self.data[key] = value
            print(self.recent, self.data)
            print('-------')
            return

        if len(self.recent) != self.cap:
            self.recent.append(key)
            self.data[key] = value
        else:
            del self.data[self.recent[-1]]
            del self.recent[-1]
            self.recent.insert(0,key)
            self.data[key] = value

        print(self.recent, self.data)
        print('-------')


# CORRECT OUTPUT:
# [null,null,null,2,null,null,-1]
obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
obj.get(1)
obj.put(3,3)
obj.get(2)
obj.put(4,4)
obj.get(1)
obj.get(3)
obj.get(4)





# Your LRUCache object will be instantiated and called as such:
#obj = LRUCache(2)
#obj.put(1, 1); # cache is {1=1}
#obj.put(2, 2); # cache is {1=1, 2=2}
#obj.get(1);    # return 1
#obj.put(3, 3); # LRU key was 2, evicts key 2, cache is 
#obj.get(2);    # returns -1 (not found)
#obj.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
#obj.get(1);    # return -1 (not found)
#obj.get(3);    # return 3
#obj.get(4);    # return 4

