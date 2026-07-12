class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) > (n - 1):
            return False

        visited = set()


        map = defaultdict(list)

        for src, dst in edges:
            map[src].append(dst)
            map[dst].append(src)  # undirected - both ways

        
        return self.dfs(0,-1, visited, map,n) and len(visited) == n


    

    def dfs(self, node, parent, visited, map,n):
        if node in visited:
            return False

        # if len(visited) == n:
        #     return True

        visited.add(node)

        for nei in map[node]:
            if nei == parent:
                continue

            if not self.dfs(nei, node, visited, map,n):
                return False 
        return True

        