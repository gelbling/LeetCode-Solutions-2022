# LeetCode 198

# INCOMPLETE

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #2 -> [7]
        #7 -> [2,9] *
        #9 -> [7,3] *
        #3 -> [9,1] *
        #1 -> [3]
        
        # start at max
        #   9, add to cant rob, remove from hash
        #      
        
        robHash = defaultdict(list)
        
        for i in range(len(nums)):
            
            if i == 0:
                robHash[nums[i]].append(nums[1])
                continue
                
            if i == len(nums)-1:
                robHash[nums[i]].append(nums[i-1])
                continue
                
            robHash[nums[i]].append(nums[i-1])
            robHash[nums[i]].append(nums[i+1])
            
        print(robHash)
                