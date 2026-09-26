class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

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

        for i in range(numCourses):
            if not self.dfs(i, check, map):
                return False


        return True



    def dfs(self, num, check, map):
        UNVISITED = 0
        VISITED = 2
        VISITING = 1

        if check[num] == VISITED:
            return True

        if check[num] == VISITING:
            return False

        check[num] = VISITING 
        for nei in map.get(num, []):
            if not self.dfs(nei, check, map):
                return False

        check[num] = VISITED
        return True






