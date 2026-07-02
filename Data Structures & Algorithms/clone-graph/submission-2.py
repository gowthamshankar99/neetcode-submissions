"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraphDFS(self, node: Optional['Node']) -> Optional['Node']:
        map = {}

        def dfs(node):
            if node in map:
                return map[node]

            # if the node is not present 
            copy = Node(node.val)
            map[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy 

        return dfs(node) if node else None

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val)  

        while queue:
            size = len(queue)
            for _ in range(size):
                current = queue.popleft()

                for neighbor in current.neighbors:
                    if neighbor not in visited:
                        visited[neighbor] = Node(neighbor.val)
                        queue.append(neighbor)
                
                    visited[current].neighbors.append(visited[neighbor])
        
        return visited[node]
                    


               

        
        
