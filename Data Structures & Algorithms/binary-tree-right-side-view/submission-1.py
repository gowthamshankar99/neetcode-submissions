# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        result = []

        queue = deque()
        queue.append(root)
        result.append(root.val)

        while queue:

            size = len(queue)
            temp_arr = []
            for i in range(size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                    temp_arr.append(node.left.val)

                if node.right:
                    queue.append(node.right)
                    temp_arr.append(node.right.val)
            if len(temp_arr) > 0:
                result.append(temp_arr[len(temp_arr)-1]) 
        return result

            

        
        