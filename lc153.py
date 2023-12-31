class Solution:
    def findMin(self, nums: List[int]) -> int:
        mid = len(nums) // 2
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l+r)//2
            if nums[m] < nums[m-1]:
                return nums[m]
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        return nums[l]