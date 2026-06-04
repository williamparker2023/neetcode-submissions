# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val>q.val:
            return self.lowestCommonAncestor(root,q,p)
        if not root.val:
            return None
        if p.val<=root.val and root.val<=q.val:
            return root
        elif p.val>root.val:
            temp = self.lowestCommonAncestor(root.right,p,q)
            if temp != None:
                return temp
            else:
                return root
        else:
            temp = self.lowestCommonAncestor(root.left,p,q)
            if temp != None:
                return temp
            else:
                return root