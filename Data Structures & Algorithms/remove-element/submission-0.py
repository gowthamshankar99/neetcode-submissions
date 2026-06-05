class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
            if value is not val
            set the val and move the counter        
        """

        counter = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[counter] = nums[i]
                counter = counter + 1
        

        return counter

