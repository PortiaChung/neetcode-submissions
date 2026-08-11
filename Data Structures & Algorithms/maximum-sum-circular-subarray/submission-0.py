class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        pre = min_pre = max_pre = 0
        maxS = float("-inf")
        minS = float("inf")
        for x in nums:
            pre += x
            maxS = max(maxS,pre-min_pre)
            minS = min(minS,pre-max_pre)
            min_pre = min(min_pre,pre)
            max_pre = max(max_pre,pre)
        if maxS < 0:
            return maxS
        else:
            return max(maxS, sum(nums)-minS)

        