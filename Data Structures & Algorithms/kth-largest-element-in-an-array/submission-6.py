class Solution:
    def findKthLargest(self, nums, k):

        """
            create maxheap

            push the values to maxheap 

            get the kth value
        """
        nums = [-num for num in nums] 
        heapq.heapify(nums)

        while k > 1:
            heapq.heappop(nums)
            k -= 1

        return -nums[0]
        