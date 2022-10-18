# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, node, res):
        if not node:
            return []
        res += self.inOrder(node.left, [])
        res += [node.val]
        res += self.inOrder(node.right, [])
        return res
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = self.inOrder(root, [])
        print(res)
        return res[k-1]