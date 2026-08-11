# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return float("inf"),float("-inf")
            l_min,l_max = dfs(node.left)
            r_min,r_max = dfs(node.right)
            x = node.val
            #左边所有节点 < 当前节点 < 右边所有节点
            if x <= l_max or x >=r_min:
                return float("-inf"),float("inf")
            return min(l_min,x),max(r_max,x)
        return dfs(root)[0]!=float("-inf")
