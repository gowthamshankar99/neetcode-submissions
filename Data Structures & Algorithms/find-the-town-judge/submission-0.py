class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        # create the adj list 

        # loop through the lit and find the key that has empty arrray - else -1

        # check if its in the nei - else - 1


        map = {}

        for src, dst in trust:
            if src not in map:
                map[src] = []
            if dst not in map:
                map[dst] = []

            map[src].append(dst)

        judge = None
        
        for key,value in map.items():
            if not value:
                judge = key


        for key, value in map.items():
            if judge != key:
                # check if jugge in value 
                if judge not in value:
                    return -1

        return judge
        