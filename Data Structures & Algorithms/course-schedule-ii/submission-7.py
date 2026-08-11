class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = [[] for _ in range(numCourses)]
        deg = [0]*numCourses

        for a,b in prerequisites:
            g[b].append(a)
            deg[a]+=1
        
        q = deque([i for i,d in enumerate(deg) if d == 0])

        res = []
        cnt = 0
        while q:
            x = q.popleft()
            res.append(x)
            cnt +=1
            for y in g[x]:
                deg[y] -=1
                if deg[y] == 0:
                    q.append(y)
        return res if cnt == numCourses else []











