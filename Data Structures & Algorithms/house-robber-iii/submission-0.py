# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dpVals = {}
        def dp(r,take):
            if r in dpVals and dpVals[r][take] != -1:
                return dpVals[r][take]
            val = 0
            if not r:
                val = 0
            elif take==1:
                val = r.val + dp(r.left,0) + dp(r.right,0)
            else:
                val = max(dp(r.left,1), dp(r.left,0)) + max(dp(r.right,1), dp(r.right,0))
            if r not in dpVals:
                dpVals[r] = [-1,-1]
            dpVals[r][take] = val
            return val

        big = 0
        if not root:
            return big
        big = dp(root,1)
        big = max(big, dp(root,0))

        return big
