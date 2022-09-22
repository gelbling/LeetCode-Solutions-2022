class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
               
        # HASH TABLE SOLUTION
        # RUNTIME: O(N)
        # MEMORY : O(N)
        valid = {}
        for i in range(len(numbers)):
            if target-numbers[i] in valid:
                return [valid[target-numbers[i]]+1,i+1]
            valid[numbers[i]] = i
            
        
        # TWO POINTERS SOLUTION
        # O(N)
        # O(1)
        p1 = 0
        p2 = len(numbers)-1
        
        while True:
            
            if numbers[p1] + numbers[p2] > target:
                p2 -= 1
            elif numbers[p1] + numbers[p2] < target:
                p1 += 1
            else:
                return [p1+1,p2+1]
                
                