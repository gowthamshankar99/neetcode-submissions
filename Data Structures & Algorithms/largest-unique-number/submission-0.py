class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:


        """
            loop through the key value pair 

            keep a max value 

            if the current value is larger than max and occurance is 1 - then update max

            return max
        """

        table = {}
        max = -1
        for num in nums:
            table[num] = table.get(num,0) + 1

        for key,value in table.items():
            if key > max and value == 1:
                max = key

        return max

        