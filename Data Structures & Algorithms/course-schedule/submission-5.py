class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if len(prerequisites) == 0:
            return True

        map = {}

        for a, b in prerequisites:
            if a not in map:
                map[a] = []
            if b not in map:
                map[b] = []
            map[a].append(b)          

        check = [0]*numCourses

        """
            0 - unvisited
            1 - visiting
            2 - visited
        """

        print(check)
        def dfs(num):
            if check[num] == 1:
                return False # cycle detcted
            if check[num] == 2:
                return True # already processed

            # make the current element as visiting 
            check[num] = 1

            for neighbor in map.get(num, []):
                if not dfs(neighbor):
                    return False
            
            check[num] = 2 # make the element as visited
            return True

        for n in range(numCourses):
            if check[n] == 0:
                if not dfs(n):
                    return False

        return True  # No cycle found anywhere