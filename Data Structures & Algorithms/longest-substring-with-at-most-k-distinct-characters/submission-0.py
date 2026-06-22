class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """

            remove the startng
        """
        n = len(s)
        left = 0
        map = collections.Counter()
        max_res = 0

        for right in range(n):
            map[s[right]] += 1

            if len(map) > k:
                while len(map) > k:
                    map[s[left]] -= 1

                    if map[s[left]] == 0:
                        del map[s[left]]

                    left +=1
            

            max_res = max(max_res, (right-left+1))

        return max_res

        