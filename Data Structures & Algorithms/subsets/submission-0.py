class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr_subset, total_subset = [],[]
        self.helper(0, nums, curr_subset, total_subset)
        return total_subset
        

    def helper(self, i, nums, curr_subset, total_subset):
        if i >= len(nums):
            total_subset.append(curr_subset.copy())
            return 
        
        curr_subset.append(nums[i])

        self.helper(i+1, nums, curr_subset, total_subset)
        curr_subset.pop()
        self.helper(i+1, nums, curr_subset, total_subset)

