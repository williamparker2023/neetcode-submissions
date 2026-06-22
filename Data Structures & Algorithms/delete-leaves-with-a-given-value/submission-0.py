# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(r):
            #returns 0 if r is None, 1 if leaf, 2 else
            if not r:
                return 0
            left = dfs(r.left)
            if left == 0:
                r.left = None
            right = dfs(r.right)
            if right == 0:
                r.right = None

            leaf = False

            if left == 0 and right == 0:
                leaf = True
            if leaf and r.val == target:
                return 0
            else:
                return 1
        ans = dfs(root)
        if ans == 0:
            return None
        return root