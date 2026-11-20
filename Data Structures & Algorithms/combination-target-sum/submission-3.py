class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr, total = [],[]
        self.helper(0, target, curr, total, nums)
        return total

    def helper(self, i, target, curr, total, nums):
        if sum(curr) > target or i >= len(nums):
            return 
        if sum(curr) == target:
            total.append(curr.copy())
            return 



        # add element 
        curr.append(nums[i])
        self.helper(i, target, curr, total, nums)
        curr.pop()
        self.helper(i+1, target, curr, total, nums)


        