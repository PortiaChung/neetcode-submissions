class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        pre = prices[0]
        for p in prices:
            res = max(res,p-pre)
            pre = min(pre,p)
        return res









