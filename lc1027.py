class Solution:
    
    def longestArithSeqLength(self, nums: List[int]) -> int:
        d = {}
        # Checking differences, so we can start at one
        for i in range(1, len(nums)):
            # Zero difference counts as an arithmetic sequence, so this helps cover that case.
            # In this case, you just want to tack on the number of occurrences of that number.
            if (0, nums[i]) in d:
                d[(0, nums[i])]+=1
            # With each pass, you check all differences up to the point you're at in the list.
            for j in range(i):
                diff = nums[i]-nums[j]
                if not nums[i]-nums[j]:
                    # OBOE if you start this counter at one.
                    if not (0, nums[i]) in d:
                        print(i)
                        d[0, nums[i]] = 0
                    else:
                        continue
                nxt = nums[i]+diff
                if not (diff, nums[i]) in d:
                    d[diff, nxt]=1
                else:
                    d[diff, nxt] = d[diff, nums[i]]+1
        return max(d.values())+1
