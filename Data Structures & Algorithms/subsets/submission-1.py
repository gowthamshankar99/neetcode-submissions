class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr, total = [],[]
        self.helper(0, curr, total, nums)
        return total


    def helper(self, index, curr, total, nums):
        if index >= len(nums):
            total.append(curr.copy())
            return

        curr.append(nums[index])
        self.helper(index+1, curr, total, nums)
        curr.pop()
        self.helper(index+1, curr, total, nums)

        


        