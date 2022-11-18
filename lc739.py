from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = deque()
        for i, val in enumerate(temperatures):
            while stack and stack[-1][1] < val:
                res[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append((i, val))
        return res
