class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for lst in intervals:
            if res and lst[0] <= res[-1][-1]:
                res[-1][-1] = max(lst[1],res[-1][-1])
            else:
                res.append(lst)
        return res
        