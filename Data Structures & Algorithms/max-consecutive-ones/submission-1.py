class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = cnt = 0
        for x in nums:
            if x:
                cnt +=1
                mx = max(cnt,mx)
            else:
                cnt = 0
        return mx