class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        
        start = 0
        end = len(s)-1

        self.reverseWord(start, end, s)

        sub_start = 0
        sub_end = 0
        while sub_end <= len(s)-1:

            if s[sub_end] == " " or sub_end == len(s)-1:
                word_end = sub_end-1 if s[sub_end] == " " else sub_end
                self.reverseWord(sub_start, word_end, s)
                sub_start = sub_end+1
                sub_end = sub_end+1
            else:
                sub_end = sub_end+1
            






    def reverseWord(self, start, end, word):
        while start < end:
            temp = word[start]
            word[start] = word[end]
            word[end]= temp

            start = start + 1
            end = end - 1        
