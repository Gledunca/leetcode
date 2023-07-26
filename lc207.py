class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        def dfs(node):
            # Cycle Check
            if node in visited:
                return False
            # No prereqs
            if not d.get(node, 0):
                return True
            # Add to visited
            visited.add(node)
            # Make sure its babies are dfs-able
            for req in d[node]:
                if not dfs(req):
                    return False
            # Remove node so future iterations dont get confused
            visited.remove(node)
            d[node] = []
            return True



        d = {}
        # Construct Adjacency List
        for req in prerequisites:
            if req[0] in d:
                d[req[0]].append(req[1])
            else:
                d[req[0]] = [req[1]]
        # How do you know where to start?
        for start_point in d:
            if not dfs(start_point):
                return False
        return True