"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        map = {}

        def dfs(node):

            # check if the node exist in the map 
            if node in map:
                return map[node]

            # if the node doesnt exist in the map 
            # create a new node 
            copy = Node(node.val)
            map[node] = copy

            for nei in node.neighbors:
                # create copy of nei
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None

        
        

        


               

        
        
