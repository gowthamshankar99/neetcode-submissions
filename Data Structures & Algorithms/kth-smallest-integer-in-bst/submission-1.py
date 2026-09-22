class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.ans = None
        
        self.inorder(root)
        return self.ans

    def inorder(self, node):
        if not node or self.ans is not None:
            return
        self.inorder(node.left)
        self.k -= 1
        if self.k == 0:
            self.ans = node.val
            return
        self.inorder(node.right)        