# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def Dfs(self, root: Optional[TreeNode]) -> int:
            nonlocal res

            if root is None:
                return 0
            leftmax = Dfs(self, root.left)
            rightmax = Dfs(self, root.right)
            res = max(res, leftmax+ rightmax)

            return 1 + max(leftmax, rightmax)
        Dfs(self, root)
        return res
        
        