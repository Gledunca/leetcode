class Solution:
    def convert(self, s: str, numRows: int) -> str:
        s = list(s)
        res = []
        strs = []

        #The top row's letters will always be spaced apart this far
        skip_size = ((numRows - 2) * 2) + 1 if numRows > 1 else 0
        
        # Add the first row in the zigzag, and then split the string into sections
        while s:
            res.append(s[0])
            s.pop(0)
            cur = []
            strs.append(s[:skip_size])
            del s[:skip_size]
        
        if len(strs[-1]) < skip_size:
            strs[-1] += [""] * (skip_size-(len(strs[-1])))

        # The rule here will go like this:
            # 1. The zigzag string will iterate over each of these substrings, in order
            #    and on each iteration, it will take the first and last from each (unless
            #    it's the last substring (take only the first), or the
            #    section only has one character left)
            # 2. Each iteration, remove from the subsection whatever you added to result.
        numRows -= 1

        while numRows:
            for i in range(len(strs)):
                if not strs[i]:
                    continue
                res.append(strs[i][0])
                strs[i].pop(0)
                if strs[i]:
                    res.append(strs[i][-1])
                    strs[i].pop(-1)

            numRows -= 1
        return "".join(res)
