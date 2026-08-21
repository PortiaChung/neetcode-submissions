class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        l,r = 0,n-1
        while l < r:
            if heights[l] > heights[r]:
                res = max(res,(r-l)*heights[r])
                r-=1
            elif heights[l] < heights[r]:
                res = max(res,(r-l)*heights[l])
                l+=1
            else:
                res = max(res,(r-l)*heights[l])
                l+=1
                r-=1

        return res

        