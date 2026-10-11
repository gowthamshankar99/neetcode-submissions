class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:

        # is k larger than s 
        if k > len(s):
            return 0

        if len(s) == 1:
            return 1

        start = 0 
        end = start+k
        res = 0 
        while end <= len(s):
            if self.duplicateCheck(s[start:end]):
                res += 1
            end +=1
            start+=1            

        return res


    def duplicateCheck(self, s):
        alpha_arr = [0]*26
        for i in s:
            index = ord(i) - ord('a')  # 97 - 97 = 0
            alpha_arr[index] += 1
            if alpha_arr[index] > 1:
                return False

        return True





                
                

                



            





        
        