class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #nums.sort()
        max_val = float('-inf')

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarray = nums[i:j+1]
                
                max_val = max(max_val, sum(subarray))

        return max_val
        