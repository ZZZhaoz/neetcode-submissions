# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            res = True

            if p and q:
                res = p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

            elif not p and not q:
                res = True

            else:
                res = False
            
            return res

        if not subRoot:
            return True

        if not root:
            return False

        if isSameTree(root, subRoot):
            return True
        else:
            return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
