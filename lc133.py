"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

import copy

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = set()
        def dfs(node: 'Node') -> 'Node':
            if not node:
                return None
            if node.val in visited:
                return None
            visited.add(node.val)
            newNode = copy.deepcopy(node)
            for item in node.neighbors:
                cp = dfs(item)
            return newNode

        return dfs(node)