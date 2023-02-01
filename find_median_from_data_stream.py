# LeetCode 295

# Solution with arrays and sorting
class MedianFinder:
    
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()

    def findMedian(self) -> float:
        
        if len(self.nums) % 2 == 0:
            midPoint = int(len(self.nums)/2)-1
            return (self.nums[midPoint]+self.nums[midPoint+1])/2
        else:
            return self.nums[int(len(self.nums)/2)]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()