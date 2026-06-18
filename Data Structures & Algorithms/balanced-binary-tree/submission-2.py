# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
        
    # def height(self, root: Optional[TreeNode]) -> bool:
    #     if root is None:
    #         return 0
        
    #     else:
    #         return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]):

            if root is None:
                return True, 0
        
            a = dfs(root.left)
            b = dfs(root.right)
            balanced = a[0] and b[0] and abs(a[1] - b[1]) <= 1
            return balanced, 1 + max(a[1], b[1])
        
        return dfs(root)[0]

        