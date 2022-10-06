# LeetCode 121

class Solution:
    def maxProfit(self, prices) -> int:

        buyPointer   = 0
        sellPointer  = 1
        maxProfit    = 0

        while (sellPointer < len(prices)):

            # profitable?
            if prices[buyPointer] < prices[sellPointer]:
                profit      = prices[sellPointer] - prices[buyPointer]
                maxProfit   = max(maxProfit,profit)
            else:
                buyPointer = sellPointer

            sellPointer += 1

        return(maxProfit)

            

obj = Solution()
obj.maxProfit([7,1,5,3,6,4])
#obj.maxProfit([1,2])