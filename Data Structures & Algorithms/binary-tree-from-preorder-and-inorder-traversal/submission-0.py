# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
       
        idx = {x: i for i,x in enumerate(inorder)}
        def dfs(prel,prer,inl,inr):
            if prel == prer:
                return 
            leftsize = idx[preorder[prel]] - inl
            left = dfs(prel+1,prel+leftsize+1,inl,inl+leftsize)
            right = dfs(prel+leftsize+1,prer,inl+leftsize+1,inr)
            return TreeNode(preorder[prel],left,right)
        return dfs(0,len(preorder),0,len(inorder))