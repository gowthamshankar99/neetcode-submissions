class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        starting_element = nums[0]
        res = 0
        
        temp = k 
        while True:
            starting_element = starting_element + 1
            if starting_element in nums:
                continue
            else:
                res = starting_element
                temp -= 1

            if temp == 0:
                break

        return res
        