class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        valid tree: n node, n-1 edges, all connected. no cycle
        how to check connected? 
        1.use bfs bcz a valid tree must be has n-1 edges just iter it
        and use a vis set to track does it include all nodes, 
        2.if has more than n-1 edges must 
        cycle exists
        """
        if len(edges) >= n:
            return False
        g = [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        q = deque([0])
        vis = set([0])
        while q:
            x = q.popleft()
            for y in g[x]:
                if y not in vis:
                    vis.add(y)
                    q.append(y)
        return len(vis) == n
       

       
            
        