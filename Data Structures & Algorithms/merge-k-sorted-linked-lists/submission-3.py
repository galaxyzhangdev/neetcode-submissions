# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        vals = []

        for l in lists:
            while l:
                vals.append(l.val)
                l = l.next

        vals.sort()
        dummy = cur = ListNode()
        for val in vals:
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next
            