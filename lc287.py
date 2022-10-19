class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        tail = nums[0]
        head = nums[nums[0]]
        # This is a graph cycle problem, using indices as pointers.
        # [1,3,4,2,5]
        while tail!=head:
            tail = nums[tail]
            head = nums[nums[head]]

        head = 0
        while True:
            tail = nums[tail]
            head = nums[head]
            if tail == head:
                break
        return tail