import bisect

class TimeMap:

    def last(self, l):
        return l[-1]

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.d:
            self.d[key] = [(value, timestamp)]
        else:
            bisect.insort(self.d[key], (value, timestamp), key=self.last)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        if timestamp < self.d[key][0][1]:
            return ""
        l, r = 0, len(self.d[key])-1
        i = r//2
        while l < r:
            if timestamp == self.d[key][i][1]:
                return self.d[key][i][0]
            if timestamp > self.d[key][i][1]:
                l = i+1
            else:
                r = i
            i = (l+r) // 2
            if l == r:
                if timestamp < self.d[key][i][1]:
                    i -= 1
                break

        return self.d[key][i][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)