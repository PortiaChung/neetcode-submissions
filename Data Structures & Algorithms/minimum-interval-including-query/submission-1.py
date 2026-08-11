class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries = sorted((x,i) for i,x in enumerate(queries))
        m,n = len(intervals), len(queries)
        j = 0
        res = [-1]*n
        h = []
        for x,i in queries:
            while j< m and intervals[j][0] <= x:
                a,b = intervals[j]
                length = b-a+1
                heapq.heappush(h,(length,b))
                j+=1
            while h and h[0][1] < x:
                heapq.heappop(h)
            
            if h:
                res[i] = h[0][0]
        return res


        