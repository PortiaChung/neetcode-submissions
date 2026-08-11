class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        1->0 take1 then take 0
        true finish. cycle cant finish
        topologic sort
        first build adj_list
        """
        g = [[] for _ in range(numCourses)]
        vis = [0]*numCourses

        deg = [0]*numCourses
        for a,b in prerequisites:
            g[b].append(a)
            deg[a]+=1   

        def dfs(x):
            vis[x] = 1
            for y in g[x]:
                if vis[y] == 1 or vis[y] == 0 and dfs(y):
                    return True
            vis[x]=2
            return False
        

        for i,v in enumerate(vis):
            if v == 0 and dfs(i):
                return False
        return True


         





        # q = deque([i for i,d in enumerate(deg) if d == 0])
        # cnt = 0
        # while q:
        #     x = q.popleft()
        #     cnt+=1
        #     for y in g[x]:
        #         deg[y] -=1
        #         if deg[y] == 0:
        #             q.append(y)
        # return True if cnt == numCourses else False


       