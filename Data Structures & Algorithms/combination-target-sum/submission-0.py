class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr_combination, total_combination = [],[]
        self.helper(0, nums, curr_combination, total_combination, target)
        return total_combination 


    def helper(self, i, nums, curr_combination, total_combination, target):
        print(sum(curr_combination))
        if sum(curr_combination) == target:
            total_combination.append(curr_combination.copy())
            return 

        if i >= len(nums) or sum(curr_combination) > target:
            return
        
        curr_combination.append(nums[i])

        self.helper(i, nums, curr_combination, total_combination, target)

        curr_combination.pop()

        self.helper(i+1, nums, curr_combination, total_combination, target)
        