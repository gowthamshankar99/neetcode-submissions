class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        element_check = len(nums)/2
        map_check = {}

        for i in range(len(nums)):
            if nums[i] in map_check:
                map_check[nums[i]] = map_check[nums[i]] + 1
            else:
                map_check[nums[i]] = 1

        for key, value in map_check.items():
            if value > element_check:
                return key

                

        