# LeetCode 155

# ALL OPERATIONS IN CONSTANT TIME

class Node:
    def __init__(self,currVal,currMin):
        self.val = currVal
        self.min = currMin

class MinStack:

    def __init__(self):
        self.stack = []

    # Time Complexity O(1)
    def push(self, val: int) -> None:
        
        if not self.stack:
            self.stack.append(Node(val,val))
            return
            
        currMin = self.stack[-1].min
            
        if val < currMin:
            self.stack.append(Node(val,val))
            return
        
        self.stack.append(Node(val,currMin))
    
    # Time Complexity O(1)
    def pop(self) -> None:
        self.stack.pop()

    # Time Complexity O(1)
    def top(self) -> int:
        return self.stack[-1].val

    # Time Complexity O(1)
    def getMin(self) -> int:
        return self.stack[-1].min
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()