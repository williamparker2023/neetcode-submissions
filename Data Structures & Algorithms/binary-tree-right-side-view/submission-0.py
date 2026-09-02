# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def dfs(r, dep):
            if not r:
                return
            if dep >= len(ans):
                ans.append(r.val)
            dfs(r.right, dep+1)
            dfs(r.left, dep+1)

        dfs(root,0)

        return ans