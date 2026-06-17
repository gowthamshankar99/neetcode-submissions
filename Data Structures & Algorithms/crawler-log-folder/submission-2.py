class Solution:
    def minOperations(self, logs: List[str]) -> int:

        """
            ends with / and one but last cahracter is not . count 1

            ends with / and contains . then - do nothing 

            ends with / and contains .. then -1 
        """

        count = 0
        for log in logs:
            if ".." not in log and "." not in log:
                count = count + 1
            elif ".." in log and count != 0:
                count = count - 1

        return count if count > 0 else 0



        