class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        res = [1]*len(nums)

        for i in range(len(nums)):

            for j in range(i):
                if nums[i] > nums[j]:
                    res[i] = max(res[i], res[j]+1)

        return max(res)



    #     total, curr, res = [],[], 0
    #     self.helper(0, total, curr, nums)
    #     #print(total)
        
    #     for single in total:
    #         if self.check_increasing(single):
    #             res = max(res, len(single))
    #     return res


    # def helper(self, index, total, curr, nums):
    #     if len(nums) == index:
    #         total.append(curr.copy())
    #         return total

    #     curr.append(nums[index])
    #     self.helper(index+1, total, curr, nums)

    #     curr.pop()
    #     self.helper(index+1, total, curr, nums)


    # def check_increasing(self, nums):
    #     for i in range(1, len(nums)):
    #         if nums[i] <= nums[i-1]:
    #             return False
    
    #     return True
            


        