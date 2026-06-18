# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def Dfs(self, root: Optional[TreeNode]) -> int:
            

            if root is None:
                return 0
            
            leftpath = Dfs(self, root.left)
            rightpath = Dfs(self, root.right)
            leftmax = max(leftpath, 0)
            rightmax = max(rightpath, 0)
            res[0] = max(res[0], root.val + leftmax + rightmax)
            return root.val + max(leftmax, rightmax)
        Dfs(self, root)
        return res[0]
        