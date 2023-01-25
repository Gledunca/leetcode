class Solution:
    def first(self, l: list):
        return l[0]
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=self.first)
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                del intervals[i+1]
            else:
                i += 1
        return intervals