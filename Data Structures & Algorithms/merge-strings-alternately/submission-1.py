class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        result = ""
        counter = 0
        result = []

        while counter < len(word1) or counter < len(word2):
        
            if counter<len(word1):
                result.append(word1[counter])
            
            if counter<len(word2):
                result.append(word2[counter])

            counter = counter + 1
            
        if counter < len(word1):        
            for i in range(counter, len(word1)):
                result.append(word1[i])
        # if counter < len(word1):
        #     result = result + word1[counter:]


        if counter < len(word2):
            # result = result + word2[counter:]
            for i in range(counter, len(word2)):
                result.append(word2[i])            


        return "".join(result)
        