class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0
        for n in s:
            if n-1 not in s:
                length=1
                while (n+length) in s:
                    length += 1
                best = max(best, length)
        return best

                    