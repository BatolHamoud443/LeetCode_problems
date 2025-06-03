from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return 0
        path = defaultdict(list)
        stack = [root]
        l = p.val
        r = q.val
        while stack:
            curr = stack.pop()
            path[curr.val].append(curr.val)
            if curr.left:
                path[curr.left.val].extend(path[curr.val])
                stack.append(curr.left)
            if curr.right:
                path[curr.right.val].extend(path[curr.val])
                stack.append(curr.right)
        # print(path)
        
        m = min(len(path[l]), len(path[r]))
        o = -1
        for i in range(m):
            if path[l][i] == path[r][i]:
                o = i
                print(o)
        if o != -1:
            return TreeNode(path[l][o])
        
        return None
