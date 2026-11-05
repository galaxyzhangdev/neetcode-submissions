# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # both of the trees are null
        if not p and not q:
            return True
        # both trees are not null
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        else:
            if not root:
                return False
            if self.isSameTree(root, subRoot):
                return True
            # left or right
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        