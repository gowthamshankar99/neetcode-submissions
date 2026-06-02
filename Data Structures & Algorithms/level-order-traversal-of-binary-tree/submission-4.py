# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        """
            create queue 
            push the root to queue 

            if length of queue is greater than 0 

            pop from queue. 

            push children to list - 
            push children to queue as well 


            return list 
        """

        queue = deque()
        res = []

        if not root:
            return res

        queue.append(root)
        res.append([root.val])

        while queue:
            inner_rest = []
            
            for i in range(len(queue)):
                
                node = queue.popleft()
                if node.left:
                    inner_rest.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    inner_rest.append(node.right.val)
                    queue.append(node.right)
            if len(inner_rest) != 0:
                res.append(inner_rest)


        return res



                

                

        
        