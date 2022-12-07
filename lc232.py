class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.insert(0, x)
        return

    def pop(self) -> int:
        while self.s1:
            self.s2.insert(0, self.s1.pop(0))
        res = self.s2.pop(0)
        while self.s2:
            self.s1.insert(0, self.s2.pop(0))
        return res

    def peek(self) -> int:
        while self.s1:
            self.s2.insert(0, self.s1.pop(0))
        res = self.s2[0]
        while self.s2:
            self.s1.insert(0, self.s2.pop(0))
        return res

    def empty(self) -> bool:
        return True if not self.s1 else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()