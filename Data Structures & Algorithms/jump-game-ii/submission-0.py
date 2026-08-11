class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        cur = nxt = 0
        for i in range(len(nums)-1):
            nxt = max(nxt,nums[i]+i)
            if i == cur:
                res +=1
                cur = nxt
        return res
        