# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:


        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)






        # list1 = self.dfs(p)
        # list2 = self.dfs(q)

        # return list1 == list2







    def dfs(self, root: TreeNode):

        if not root:
            return None
        
        queue = deque([root])
        res= []
        res.append(root.val)

        while queue:

            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    res.append(node.left.val)
                else:
                    res.append(None)
                if node.right:
                    queue.append(node.right)
                    res.append(node.right.val)
                else:
                    res.append(None)                    

        return res
                

                
                

