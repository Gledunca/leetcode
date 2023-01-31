class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        c = Counter(tasks)
        
        m = c.most_common()[0][1]
        
        f = len([i for i, num in c.items() if num == m])
        
        
        return max((m-1) * (n+1) + f, len(tasks))
        