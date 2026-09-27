# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        diff = [float('inf')]
        return self.dfs(root, target, diff)
        

    def dfs(self, root, target, diff):

        if not root:
            return

        current_diff = (abs(root.val - target), root.val)
        best_diff = (abs(diff[0] - target), diff[0])

        if current_diff < best_diff:
            diff[0] = root.val        


        if root.val < target:
            self.dfs(root.right, target, diff)

        if root.val > target:
            self.dfs(root.left, target, diff)


        return diff[0]

        