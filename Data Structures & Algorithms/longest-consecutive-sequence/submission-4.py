class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s= set(nums)
        # print(s)
        # {2, 3, 4, 5, 10, 20}
        res = 0
        for x in s:
            if x-1 in s:
                continue
            y = x+1
            while y in s:
                y +=1
            res = max(res,y-x)
         
        return res