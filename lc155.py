class MinStack:
    def __init__(self):
        self.s = []
        self.minstack = []
        return

    def push(self, val):
        if not self.minstack:
            self.minstack.insert(0, val)
        else:
            ins = min(self.minstack[0], val)
            self.minstack.insert(0, ins)
        self.s.insert(0, val)
        return
    
    def pop(self):
        self.minstack.pop(0)
        return self.s.pop(0)

    def top(self):
        return self.s[0]

    def getMin(self):
        return self.minstack[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
