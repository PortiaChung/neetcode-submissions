class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1]*n
        for i in range(1,len(nums)):
            pre[i] *= pre[i-1]
            pre[i] *= nums[i-1]
        suf = [1]*n
        for i in range(len(nums)-2,-1,-1):
            suf[i] *= suf[i+1]
            suf[i]*=nums[i+1]
        res = []
        for p,s in zip(pre,suf):
            res.append(p*s)
        return res
