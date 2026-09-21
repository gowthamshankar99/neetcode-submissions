# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        total_sum = 0 
        return self.helper(root, targetSum)


    def helper(self, root, total_sum):
        if not root:
            return False

        total_sum = total_sum - root.val

        if not root.left and not root.right:
            return total_sum == 0

        return self.helper(root.left, total_sum) or self.helper(root.right, total_sum)