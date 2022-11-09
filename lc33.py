class Solution:
    def search(self, nums , target: int) -> int:
        if len(nums) == 1 and target == nums[0]:
            return 0
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            # m is on a right side of a rotated array
            # Everything is ascending til r
            if nums[m] < nums[r]:
                if nums[m] < target and target <= nums[r]:
                    l = m+1
                else:
                    r = m
            # m is on a left side of a rotated array
            # There is a break before r
            elif nums[m] > nums[r]:
                if nums[l] <= target and target < nums[m]:
                    r = m
                else:
                    l = m+1
        return -1 if nums[l] != target else l