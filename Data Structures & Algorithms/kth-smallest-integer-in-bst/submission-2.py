class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k 
        self.ans = 0
        self.helper(root)
        return self.ans


    def helper(self, root):
        if not root:
            return 

        self.helper(root.left)

        self.k -= 1
        if self.k == 0:
            self.ans = root.val
            return 

        self.helper(root.right)