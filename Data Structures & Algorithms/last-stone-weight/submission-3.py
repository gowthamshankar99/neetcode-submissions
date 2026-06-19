class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # create maxheap      
        stones = [-s for s in stones] 
        heapq.heapify(stones)
        print(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)    

            print(first,second)        

            if second > first:
                heapq.heappush(stones, (first-second)) 

        stones.append(0)
        return abs(stones[0])

        