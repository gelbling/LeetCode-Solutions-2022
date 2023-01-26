#######################################################
#####                                              ####
##                     LeetCode 392                  ##
#####                                              ####
#######################################################
#######################################################
##############                           ##############
#########               SOLUTION 1            #########
#####              Time Complexity: O(t)          #####
#########          Space ''       : O(1)      #########
##############                           ##############
#######################################################
#######################################################

class Solution:

    def isSubsequence(self, s: str, t: str) -> bool:

        if not s:
            return True

        sPointer = 0
        tPointer = 0

        while tPointer < len(t):
            
            if s[sPointer] == t[tPointer]:
                sPointer += 1
                tPointer += 1
            else:
                tPointer += 1

            if sPointer == len(s):
                return True

        return False