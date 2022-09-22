class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0:
            return False
        
        stack = []
        
        hashe = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        for i in s:
            if i in hashe:
                if stack and stack[-1] == hashe[i]:
                    print(stack)
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
                
        if not stack:
            return True
        else:
            return False

obj = Solution()
obj.isValid("[]{}")