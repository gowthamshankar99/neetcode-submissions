class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        # Initial window of size k
        curr_w = blocks[:k].count('W')
        min_w = curr_w

        # Slide the window by one element at a time
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                curr_w -= 1
            if blocks[i] == 'W':
                curr_w += 1
            min_w = min(min_w, curr_w)

        
        return min_w


        