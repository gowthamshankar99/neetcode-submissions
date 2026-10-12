class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:


        """

        [4,2,1]

        """

        # sort the array 
        nums.sort(reverse=True)

        left = 0 
        starting = nums[left] 
        res = 0

        while left < len(nums):
            remanining = k 
            output = 1
            for i in range(left+1, len(nums)):
                
                remanining =  remanining - (nums[left] - nums[i])
                if remanining >= 0:
                    output += 1
            left +=1
        
            res = max(res, output)

        return res



        