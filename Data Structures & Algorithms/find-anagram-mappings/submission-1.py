class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:

        map = {}
        counter = 0
        for num in nums2:
            map[num] = counter
            counter += 1

        res = []
        
        for num in nums1:
            res.append(map[num])


        return res

        
        