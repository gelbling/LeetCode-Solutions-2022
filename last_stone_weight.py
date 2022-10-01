# LeetCode 1046

class Solution:
    def lastStoneWeight(self, stones: int) -> int:
        while len(stones) > 1:

            stones      = sorted(stones,reverse=True)

            firstStone  = stones[0]
            secondStone = stones[1]

            if firstStone == secondStone:
                stones.pop(0)
                stones.pop(0)
            else:
                stones.pop(1)
                stones[0] = firstStone - secondStone

        if stones:
            return stones[-1]
        else:
            return 0

obj = Solution()
obj.lastStoneWeight([2,7,4,1,8,1])
obj.lastStoneWeight([1])
obj.lastStoneWeight([2,2])