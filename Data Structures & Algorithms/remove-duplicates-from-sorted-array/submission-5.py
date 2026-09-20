class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # 'left' tracks the index of the last placed unique element
        left = 0 
        
        # 'right' scans through the array starting from the second element
        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
                
        # The number of unique elements is the index + 1
        return left + 1
