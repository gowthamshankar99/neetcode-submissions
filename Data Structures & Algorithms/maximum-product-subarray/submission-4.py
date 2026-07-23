import math
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = float('-inf')
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarray = nums[i:j+1]
                res = max(res, math.prod(subarray))
                
        return res