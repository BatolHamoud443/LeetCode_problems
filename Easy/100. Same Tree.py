# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q != None:
            return False
        if p != None and q == None:
            return False
        if p == None and q == None:
            return True

        f = deque([p])
        s = deque([q])
        while f:
            node1 = f.popleft()
            node2 = s.popleft()

            if node1.val != node2.val:
                
                return False
            
            if node1.left and node2.left:
                f.append(node1.left)
                s.append(node2.left)
            
            if bool(node1.left) != bool(node2.left):
                return False

            if node1.right and node2.right:
                f.append(node1.right)
                s.append(node2.right)

            if bool(node1.right) != bool(node2.right):
                return False
    
        return True 
