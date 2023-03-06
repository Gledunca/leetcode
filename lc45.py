class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        l, r = 0, 0
        j = 0
        i = 0
        end = len(nums)-1
        while r < end:
            maxjump = max([pos+l+jump for pos, jump in enumerate(nums[l:r+1])])
            l = r+1
            r=maxjump
            j += 1
        return j
            