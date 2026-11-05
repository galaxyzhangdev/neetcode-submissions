# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            # already reach the left end 
            cur = cur.right



    #     res = []
    #     self.add_node(root, res)
    #     return res[k-1]

    # def add_node(self, root, res):
    #     if root:
    #         self.add_node(root.left, res)
    #         res.append(root.val)
    #         self.add_node(root.right, res)
