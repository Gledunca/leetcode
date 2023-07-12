class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def cycleCheck(node, visited, res):
            if node in visited:
                return True
            if node in res:
                return False
            cycle = False
            visited.add(node)
            for i in graph[node]:
                if not i in visited:
                    cycle = cycle or cycleCheck(i, visited, res)
                else:
                    return True
            visited.remove(node)
            if not cycle:
                res.add(node)
            return cycle

        res = set()
        for i in range(len(graph)):
            if not graph[i]:
                res.add(i)
                continue
            if i in res:
                continue
            if cycleCheck(i, set(), res):
                continue
            else:
                res.add(i)
        return sorted(list(res))