# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        ind = int(len(nums)/2)
        root = TreeNode(nums[ind])
        q = deque()
        q.append((root, 0, ind-1))
        q.append((root, ind+1, len(nums)-1))
        
        while q:
            p,l,r = q.popleft()
            if l <= r:
                i = (l+r)//2
                c = TreeNode(nums[i])
                if c.val < p.val:
                    p.left = c
                else:
                    p.right = c
                q.append((c,l,i-1))
                q.append((c, i+1,r))
        return root
