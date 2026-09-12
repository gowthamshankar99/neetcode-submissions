class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curr,res = [],[]
        self.helper(nums, curr, res)
        return res


    def helper(self, nums, curr, res):
        if len(curr) == len(nums):
            res.append(curr.copy())
            return 

        for i in nums:
            if i not in curr:
                curr.append(i)
                self.helper(nums, curr, res)
                curr.pop()

        