

class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.memo = {}
        index = 0

        return self.helper(0, nums, target, index)
        
    def helper(self, current_sum, nums, target, index):
        # memoize here 
        if (index, current_sum) in self.memo:
            return self.memo[(index, current_sum)]
        if index == len(nums):
            if current_sum == target:
                return 1
            else:
                return 0
        

        # left side 
        left = self.helper(current_sum+nums[index], nums, target, index+1)
        # right side
        right = self.helper(current_sum-nums[index], nums, target, index+1)
        self.memo[(index, current_sum)] = left+right
        return left+right