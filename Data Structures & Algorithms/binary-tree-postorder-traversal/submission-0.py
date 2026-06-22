# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []

        def dfs(r):
            if not r:
                return
            dfs(r.left)
            dfs(r.right)
            order.append(r.val)
        dfs(root)
        return order