# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def newChild(r,val):
            if not r:
                return TreeNode(val)
            if r.val > val:
                r.left = newChild(r.left,val)
            else:
                r.right = newChild(r.right,val)
            return r
        ans = newChild(root,val)
        return ans