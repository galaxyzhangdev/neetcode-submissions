# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodeSet = set()

        cur = head
        while cur:
            if cur.val in nodeSet:
                return True
            nodeSet.add(cur.val)
            cur = cur.next
        return False
