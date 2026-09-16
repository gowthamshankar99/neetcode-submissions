class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curr, total = [],[]
        self.helper(curr, total, nums)
        return total


    def helper(self, curr, total, nums):
        if len(curr) == len(nums):
            total.append(curr.copy())
            return 


        for num in nums:
            if num not in curr:
                curr.append(num)
                self.helper(curr, total, nums)
                curr.pop()

        
        