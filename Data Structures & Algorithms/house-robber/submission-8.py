class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        # create the output array 
        res = [0]*len(nums)

        res[0] = nums[0]
        res[1] = max(nums[1], nums[0])

        for i in range(2,len(nums)):
            res[i] = max(res[i-1], nums[i]+res[i-2])

        return res[len(nums)-1]

        


        