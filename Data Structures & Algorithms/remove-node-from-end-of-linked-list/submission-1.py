# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # two pointers to keep a distance of n
        l = dummy
        r = head

        # keep a distance
        while n > 0 and r:
            r = r.next
            n -= 1
        
        # let r reaches the end
        while r:
            r = r.next
            l = l.next
        
        l.next = l.next.next

        return dummy.next


