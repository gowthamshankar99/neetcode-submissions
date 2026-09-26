class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        seen = [0]*(numCourses)

        # create adcency list 
        map = {}
        for src, dst in prerequisites:
            if src not in map:
                map[src] = []
            if dst not in map:
                map[dst] = []
            map[src].append(dst)

        order = []
        visited = set()


        for course in range(numCourses):
            if course not in visited:
                if not self.dfs(order, visited, numCourses, prerequisites,map, seen, course):
                    return []

        return order



    def dfs(self, order, visited, numCourses, prerequisites, map, seen, course):
        VISITING = 1
        VISITED = 2
        UNVISITED = 0 



        if seen[course] == VISITED:
            return True

        if seen[course] == VISITING:
            return False

        # mark course as visiting 
        seen[course] = 1            

        for nei in map.get(course, []):
            if nei not in visited:
                if not self.dfs(order, visited, numCourses, prerequisites, map, seen, nei):
                    return False

        seen[course] = VISITED

        order.append(course)
        return True




        