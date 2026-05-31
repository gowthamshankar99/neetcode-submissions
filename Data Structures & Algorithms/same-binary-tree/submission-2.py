# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        left_list = []
        right_list = []

        self.dfs(p, left_list)
        self.dfs(q, right_list)

        return left_list == right_list



    def dfs(self, root, l):
        if not root:
            l.append(None)
            return l
        
        l.append(root.val)
        self.dfs(root.left,l)
        self.dfs(root.right,l)

        