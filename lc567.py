class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_d = {}
        for i in range(len(s1)):
            s1_d[s1[i]] = s1_d.get(s1[i], 0) + 1
        # print(s1_d)
        s2_d = {}
        for i in range(len(s1)):
            s2_d[s2[i]] = s2_d.get(s2[i], 0) + 1
        # print(s2_d)
        # print(len(s1), len(s2))
        for i in range(len(s1), len(s2)):
            # print(s1_d, s2_d)
            if s1_d == s2_d:
                return True
            # print(i-len(s1))
            s2_d[s2[i-len(s1)]] -= 1
            if s2_d[s2[i-len(s1)]] == 0:
                del s2_d[s2[i-len(s1)]]
            s2_d[s2[i]] = s2_d.get(s2[i], 0) + 1
        if s1_d == s2_d:
            return True
        return False
