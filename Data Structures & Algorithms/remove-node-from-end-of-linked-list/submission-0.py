# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # left need to + 1 to remove the node
        left = dummy
        right = head

        # fix the distance first (n)
        while n > 0 and right:
            right = right.next
            n -= 1

        # let right reach the end (null)
        # same as left
        while right:
            right = right.next
            left = left.next

        left.next = left.next.next
        return dummy.next
        

