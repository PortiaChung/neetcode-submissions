# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            if not node:
                return -1
            left_len = dfs(node.left)
            right_len = dfs(node.right)
            nonlocal res
            res = max(res,left_len+right_len+2)
            return max(left_len,right_len)+1
        dfs(root)
        return res

        