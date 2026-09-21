# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        
        queue = deque()
        queue.append(root)

        # result array 
        result = []        
        result.append([root.val])


        while queue:

            size = len(queue)
            
            inner_array = []
            for i in range(size):
                
                node = queue.popleft()
                if node.left:
                    inner_array.append(node.left.val)
                    queue.append(node.left)
                
                if node.right:
                    inner_array.append(node.right.val)
                    queue.append(node.right)
            
            result.append(inner_array)

        return result[:-1]

        
        