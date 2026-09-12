class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        curr, total = [],[]
        candidates.sort()
        self.helper(0, curr, total, target, candidates)
        return total



    def helper(self, i, curr, total, target, nums):
        if sum(curr) == target:
            total.append(curr.copy())
            return 

        if i >= len(nums) or sum(curr) > target:
            return 

        # append number
        curr.append(nums[i])
        self.helper(i+1, curr, total, target, nums)
        curr.pop()

        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1

        self.helper(i+1, curr, total, target, nums)
        

        
        