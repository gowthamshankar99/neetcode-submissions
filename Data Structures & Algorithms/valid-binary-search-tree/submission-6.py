# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev_val = float('-inf')
        
        def inorder(node):
            if not node:
                return True
                
            # Visit Left Subtree
            if not inorder(node.left):
                return False
                
            # Visit Current Node (Check condition)
            if node.val <= self.prev_val:
                return False
            self.prev_val = node.val
            
            # Visit Right Subtree
            return inorder(node.right)
            
        return inorder(root)
        
    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
            
        # Initialize queue with tuples: (node, lower_bound, upper_bound)
        queue = deque([(root, float('-inf'), float('inf'))])
        
        while queue:
            node, low, high = queue.popleft()
            
            # Check if current node violates the range constraints
            if not (low < node.val < high):
                return False
                
            # Enqueue left child with updated upper bound
            if node.left:
                queue.append((node.left, low, node.val))
                
            # Enqueue right child with updated lower bound
            if node.right:
                queue.append((node.right, node.val, high))
                
        return True
