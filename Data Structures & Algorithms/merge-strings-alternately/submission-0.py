class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        result = ""
        counter = 0

        while counter < len(word1) or counter < len(word2):
        
            if counter<len(word1):
                result = result + word1[counter]
            
            if counter<len(word2):
                result = result + word2[counter]

            counter = counter + 1
            
        
        if counter < len(word1):
            result = result + word1[counter:]


        if counter < len(word2):
            result = result + word2[counter:]


        return result
        