# LeetCode 153

# Time Complexity: O(logn)

class Solution:
    def findMin(self, nums) -> int:

        while True:

            midPoint = len(nums)//2

            if len(nums) == 1:
                return nums[0]

            if len(nums) == 2:
                if nums[0] > nums[1]:
                    return nums[1]
                else:
                    return nums[0]

            if nums[len(nums)-1] < nums[0] and nums[midPoint] > nums[len(nums)-1]:
                nums = nums[midPoint:]
                continue

            if nums[midPoint-1] > nums[midPoint+1]:
                nums = nums[midPoint:]
            else:
                nums = nums[:midPoint]


            

            