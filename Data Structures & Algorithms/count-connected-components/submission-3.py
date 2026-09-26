class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        map = {}

        for src, dst in edges:
            if src not in map:
                map[src] = []
            if dst not in map:
                map[dst] = []
            map[src].append(dst)
            map[dst].append(src)

        print(map)
        res = 0

        visited = set()
        for i in range(n):
            if i not in visited:
                
                self.dfs(edges,map,i, visited)
                res += 1
        
        return res

    def dfs(self, edges, map, i, visited):
        visited.add(i)

        for nei in map.get(i, []):
            if nei not in visited:
                self.dfs(edges, map, nei, visited)

        