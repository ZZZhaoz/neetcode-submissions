# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        res = []
        q.append(root)

        while q:
            lenq = len(q)
            level = []
            for i in range(lenq):
                node = q.popleft()
                
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level[-1])
        return res
        # res =[]
        # def dfs(root):
        #     nonlocal res 
        #     if not root:
        #         return None
        #     res.append(root.val)
        #     if root.right:  
        #         dfs(root.right)
        #     else:
        #         dfs(root.left)
            
        # dfs(root)
        
        # return res
        