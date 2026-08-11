import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[] for _ in range(n)]
        for u,v,t in times:
            g[u-1].append((v-1,t))

        dist = [float("inf")]*n
        dist[k-1] = 0
        h = [(0,k-1)]

        cnt = 0
        max_dist = 0

        while h:
            d,x = heapq.heappop(h)
            if d > dist[x]:
                continue  
            max_dist = d
            cnt+=1
            if cnt == n:
                return max_dist

            for y,t in g[x]:
                new_dist = d+t
                if new_dist < dist[y]:
                    dist[y] = new_dist
                    heapq.heappush(h,(new_dist,y))
        return -1

