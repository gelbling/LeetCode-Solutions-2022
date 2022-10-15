# LeetCode 1710

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        items = 0
        
        boxTypes.sort(key = lambda x: x[1], reverse=True)
                
        for i in boxTypes:
            
            if truckSize - i[0] >= 0:
                truckSize -= i[0]
                items += i[0] * i[1]
            else:
                for ii in range(i[0]):
                    if truckSize - 1 >= 0:
                        truckSize -= 1
                        items += 1 * i[1]
                        
        return items