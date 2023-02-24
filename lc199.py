# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    
    def lvlOrder(self, root: Optional[TreeNode]) -> List[int]:
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
        return levels
            
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        levels = self.lvlOrder(root)
        i = 1
        res = []
 
        while i in levels:
            res.append(levels[i][-1].val)
            i += 1
        return res
        
        