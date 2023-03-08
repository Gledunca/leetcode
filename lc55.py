class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = 0
        jump = nums[0]
        end = len(nums)-1
        while True:
            print(pos)
            betterFound = 0
            jump = nums[pos]
            if jump+pos >= end:
                return True
            if jump == 0:
                break
            i = 1
            while pos+i < pos+jump:
                print(i, nums[i], pos, jump)
                if pos+i+nums[pos+i] >= pos+jump:
                    print("better found")
                    betterFound = 1
                    break
                i += 1
            if betterFound == 1:
                pos = pos+i
                jump = nums[pos]
            else:
                pos = pos+jump
                jump = nums[pos]
                
                    
        return False