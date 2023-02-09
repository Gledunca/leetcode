class Solution:
    def numDecodings(self, s: str) -> int:
        d = {len(s): 1}
        
        for i in range(len(s)-1, -1, -1):
            print("i", i)
            if s[i] == "0":
                d[i] = 0
            
            else:
                d[i] = d[i+1]
            
            if (i < (len(s) - 1)) and ((s[i] == "1") or (s[i] == "2" and int(s[i+1]) in range(0, 7))):
                d[i] += d[i+2]
                
        print(d)
            
        return d[0]
        