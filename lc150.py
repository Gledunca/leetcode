from queue import LifoQueue
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = LifoQueue()
        while tokens:
            t = tokens.pop(0)
            if t == "+":
                st.put(st.get() + st.get())
            elif t == "-":
                a = st.get()
                b = st.get()
                st.put(b - a)
            elif t == "*":
                st.put(st.get() * st.get())
            elif t == "/":
                a = st.get()
                b = st.get()
                ans = math.ceil(b/a) if ans < 0 else math.floor(b/a)
                st.put(ans)
            else:
                st.put(int(t))
            a = st.get()
            st.put(a)
        return st.get()