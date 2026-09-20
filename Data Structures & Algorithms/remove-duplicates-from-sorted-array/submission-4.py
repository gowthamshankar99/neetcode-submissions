class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        new_set = set()

        for num in nums:
            new_set.add(num)

        list1 = list(new_set)
        list1.sort()

        counter = 0
        for val in list1:
            nums[counter] = val
            counter += 1

        while counter < len(nums):
            nums[counter] = 0
            counter += 1

        return len(list1)