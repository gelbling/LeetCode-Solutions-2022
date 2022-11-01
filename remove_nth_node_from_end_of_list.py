# LeetCode 19

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time Complexity  : O(n)
# Space COmplexity : O(1)
class Solution:
    def removeNthFromEnd(self, head, n: int):

        # if there is one element, return None
        if not head.next:
            return None
        
        # start both pointers at head
        p1 = head
        p2 = head
        
        # increment fast pointer by n
        for i in range(n):
            p2 = p2.next
        
        # traverse to the end of the linked list
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next
        
        # if p2 is None, return p1.next
        if not p2:
            return p1.next
        
        # get the next value
        skip = p1.next.next
        # apply the skip
        p1.next = skip
        
        # return the head
        return head