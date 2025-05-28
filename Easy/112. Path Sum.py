# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        s = [(root, root.val)]
        while s:
            curr, val = s.pop()
            if not curr.right and not curr.left and val == targetSum:
                return True
            if curr.left:
                s.append((curr.left, val + curr.left.val))
            if curr.right:
                s.append((curr.right, val + curr.right.val))
        return False
