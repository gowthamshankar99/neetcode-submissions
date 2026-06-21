class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, k-1
        min_value = sys.maxsize
        while r < len(nums):

            min_value = min(min_value, nums[r]-nums[l])
            l += 1
            r += 1

        return min_value

        
        