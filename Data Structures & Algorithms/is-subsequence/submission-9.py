class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        length_t = len(t)
        length_s = len(s)

        s_counter = 0
        t_counter = 0

        if s == "" and t == "":
            return True
        
        if s == "":
            return True

        while t_counter<length_t:
            if s[s_counter] != t[t_counter]:
                t_counter = t_counter + 1
            else:
                t_counter = t_counter + 1
                s_counter = s_counter + 1

            if s_counter == len(s):
                return True



        return False            


        