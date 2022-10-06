######################################
########## INITIAL SOLUTION ##########
######################################
from multiprocessing import current_process


class Solution:
    def combinationSum(self, candidates: int, target: int) -> list:

        output = []
        
        for i in candidates:

            currCandidates = candidates

            while currCandidates:

                totalSum = 0

                #if max(currCandidates)+totalSum > target:
                #   break

                for ii in currCandidates:
                    sum = []
                    if totalSum + i < target or totalSum + ii < target:
                        totalSum = i+ii
                    elif totalSum + i == target:
                        sum.append(i)
                        sum.append(i)
                        currCandidates.pop(i)
                    elif totalSum + ii == target:
                        sum.append(ii)
                        sum.append(ii)
                        currCandidates.pop(ii)
                    else:
                        currCandidates.pop(ii)

                    if sum:
                        return sum

                    print(output)
                    




candidates = [2,3,6,7]
target = 7

obj = Solution().combinationSum(candidates, target)