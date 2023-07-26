class Node:
    def __init__(self, key, value, prev, nxt):
        self.key = key
        self.val = value
        self.p = prev
        self.n = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.capacity = capacity
        self.recency = []
        self.left = None
        self.right = None

    
    def insert(self, new: Node) -> None:
        if not (self.left or self.right):
            self.left = self.right = new
        elif self.left == self.right:
            self.left.n = new
            new.p = self.left
            self.right = new
        else:
            self.right.n = new
            new.p = self.right
            self.right = new

        

    def remove(self, cur):
        # Only one item in the list
        if self.left == self.right:
            self.left = self.right = None
        # Item is the leftmost
        elif self.left == cur:
            self.left = self.left.n
        # Item is the rightmost
        elif self.right == cur:
            self.right = self.right.p
        # In the middle
        else:
            prev, nxt = cur.p, cur.n
            prev.n = nxt
            nxt.p = prev
        del cur
        return


    def get(self, key: int) -> int:
        if self.d.get(key):
            val = self.d[key].val
            self.remove(self.d[key])
            self.insert(self.d[key])
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.d.get(key):
            self.remove(self.d[key])
            self.d[key].val = value
            self.insert(self.d[key])
            return
        new_node = Node(key, value, None, None)
        if len(self.d.keys()) < self.capacity:
            self.insert(new_node)
        else:
            del self.d[self.left.key]
            self.remove(self.left)
            self.insert(new_node)
        self.d[key] = new_node
