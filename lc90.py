class Solution:
    def backtrack(self, s: list, nums: List[int], cur: List[int]) -> set:
        if nums == []:
            return s
        if len(s) == 0:
            s.append([])
        for i in range(len(nums)):
            cur.append(nums[i])
            if cur not in s:
                s.append(cur.copy())
            s = self.backtrack(s, nums[i+1:], cur)
            cur.pop()
        return s
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s = []
        s = self.backtrack(s, nums, [])
        return s