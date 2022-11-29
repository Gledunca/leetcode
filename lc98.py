# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root: Optional[TreeNode], min_num: int, max_num: int) -> bool:
        if not root:
            return True
        print(root.val, min_num, max_num)
        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.right.val <= root.val:
            return False
        if root.val >= max_num or root.val <= min_num:
            return False
        return self.helper(root.left, min_num, root.val) and self.helper(root.right, root.val, max_num)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, (-2 ** 31)-1, (2 ** 31))