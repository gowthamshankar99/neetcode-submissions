class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        curr, total = [],[]
        nums.sort()
        self.helper(0, curr, total, nums)
        return total


    def helper(self, index, curr, total, nums):
        if index >= len(nums):
            total.append(curr.copy())
            return

        curr.append(nums[index])
        self.helper(index+1, curr, total, nums)
        curr.pop()
        while index + 1 < len(nums) and nums[index] == nums[index+1]:
            index += 1
        self.helper(index+1, curr, total, nums)

        


        