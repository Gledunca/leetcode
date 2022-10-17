# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node: TreeNode, m: int) -> int:
        if not node:
            return 0
        res = 0
        if node.val >= m:
            res += 1
        m = max(m, node.val)
        res += self.dfs(node.left, m)
        res += self.dfs(node.right, m)
        return res

    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)