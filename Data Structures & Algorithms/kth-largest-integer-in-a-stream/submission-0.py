class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.arr = nums

        
        

    def add(self, val: int) -> int:
        # add the value 
        self.arr.append(val)
        self.arr.sort(reverse=True)
        return self.arr[self.k-1]

        
