# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        count = [0]
        count = self.dfs(root, low, high, count)
        return count[0]


    def dfs(self, root, low, high, count):
        if not root:
            return 0

        if root.val >= low and root.val <= high:
            count[0] = count[0] + root.val

        self.dfs(root.left, low, high, count)
        self.dfs(root.right, low, high, count)

        return count

        