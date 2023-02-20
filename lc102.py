# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        levels = {}
        dq = deque()
        dq.appendleft((root, 1))
        while dq:
            item = dq.pop()
            node = item[0]
            lvl = item[1]
            if lvl not in levels:
                levels[lvl] = []
            levels[lvl].append(node)
            if node.left:
                dq.appendleft((node.left, lvl+1))
            if node.right:
                dq.appendleft((node.right, lvl+1))
        res = []
        i = 1
        while i in levels:
            lvl = []
            for node in levels[i]:
                lvl.append(node.val)
            res.append(lvl)
            i += 1
        
        return res
        