# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        return self.dfs(root, root.val)



    def dfs(self, root, max_so_far):
        if not root:
            return 0

        res = 0
        if root.val >= max_so_far:
            res = 1
            max_so_far = max(root.val, max_so_far)
        
        res += self.dfs(root.left, max_so_far)
        res += self.dfs(root.right, max_so_far)

        return res
        