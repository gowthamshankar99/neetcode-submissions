import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        """

        """
        max_heap = []
        
        for gift in gifts:
            heapq.heappush(max_heap, -gift)

        for i in range(k):
            largest = heapq.heappop(max_heap)
            heapq.heappush(max_heap, -1 * math.floor(math.sqrt(abs(largest))))

        res = 0

        for val in max_heap:
            res += val
        return abs(res)
        