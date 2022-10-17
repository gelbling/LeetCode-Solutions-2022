# LeetCode 1
# Two Sum not sorted input array

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # BRUTE FORCE
        # O(N^2)
        # O(1)
        for i in range(len(nums)):
            for ii in range(len(nums)):
                if i != ii and nums[i]+nums[ii] == target:
                    return [i,ii]
        
        # OPTIMAL
        # RUNTIME: O(N)
        # MEMORY : O(N)
        valid = {}
        for i in range(len(nums)):
            
            if target-nums[i] in valid:
                return [valid[target-nums[i]],i]
            else:
                valid[nums[i]] = i