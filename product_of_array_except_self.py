#######################################################
#####                                              ####
##                     LeetCode 238                  ##
#####                                              ####
#######################################################
#######################################################
##############                           ##############
#########               SOLUTION 1            #########
#####              Time Complexity: O(n)          #####
#########          Space ''       : O(n)      #########
##############                           ##############
#######################################################
#######################################################


class Solution:
    def productExceptSelf(self, nums):

        # create prefix and postfix arrays
        prefix  = [nums[0]] * len(nums)
        postfix = [nums[-1]] * len(nums)

        # intialize pointers
        p1 = 1
        p2 = len(nums)-2

        # populate prefix and postfix arrays with sums from left to right and right to left
        for i in range(len(nums)-1):
            prefix[p1] = nums[p1] * prefix[p1-1]
            p1 += 1
            postfix[p2] = nums[p2] * postfix[p2+1]
            p2 -= 1

        # create output array
        output = [None] * len(nums)

        # loop input array and populate output array
        for i in range(len(nums)):
            if i == 0:
                output[i] = postfix[i+1]
            elif i == len(nums)-1:
                output[i] = prefix[i-1]
            else:
                output[i] = prefix[i-1] * postfix[i+1]

        return output



