# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.left is None and root.right is None:
            return root

        elif root.left is None:
            self.invertTree(root.right)
            a = root.right
            root.left = a
            root.right = None
            return root
        elif root.right is None:
            self.invertTree(root.left)
            a = root.left
            root.right = a
            root.left = None
            return root
        else:
            self.invertTree(root.left)
            self.invertTree(root.right)
            root.right, root.left = root.left, root.right
            return root






    
    