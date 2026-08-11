class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre = [0]*n
        pre[0] = height[0]
        for i in range(1,n):
            pre[i] = max(height[i],pre[i-1])
        
        suf = [0]*n
        suf[-1] = height[-1]
        for i in range(n-2,-1,-1):
            suf[i] = max(height[i],suf[i+1])

        res = 0
        for h,p,s in zip(height,pre,suf):
            mn = min(p,s)
            res+= mn-h
        return res
