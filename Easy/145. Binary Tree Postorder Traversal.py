# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def postorder(root):
            if not root:
                return []

            result.append(root.val)
            postorder(root.right)
            postorder(root.left)
            return result

        ans = postorder(root)
        return ans[::-1]
