# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def dfs(r):
            if not r:
                return
            dfs(r.left)
            arr.append(r.val)
            dfs(r.right)
        
        dfs(root)

        return arr[k-1]