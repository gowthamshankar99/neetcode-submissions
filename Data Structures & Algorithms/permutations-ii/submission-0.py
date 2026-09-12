class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        curr,res = [],[]
        used = [0]*len(nums)
        self.helper(nums, curr, res, used)
        return res


    def helper(self, nums, curr, res, used):
        
        if len(curr) == len(nums) and curr.copy() not in res:
            res.append(curr.copy())
            return 

        for i,value in enumerate(nums):
            if used[i]:
                continue

            curr.append(value)
            # mark the flag 
            used[i] = True
            self.helper(nums, curr, res, used)
            curr.pop()
            used[i] = False

        