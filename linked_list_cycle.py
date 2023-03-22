# LeetCode 141


# TWO POINTER SOLUTION (if slow and fast pointer meet, there is a cycle)
# Time Complexity: O(n)
# Space ''       : O(1)
class Solution:
    def hasCycle(self, head) -> bool:

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

# STORING SEEN NODES IN SET SOLUTION
# Time Complexity: O(n)
# Space ''       : O(n)
class Solution:
    def hasCycle(self, head) -> bool:

        if not head:
            return False

        visited = set()
        curr = head

        while curr.next:
            visited.add(curr)
            if curr.next in visited:
                return True
            else:
                curr = curr.next

        return False
