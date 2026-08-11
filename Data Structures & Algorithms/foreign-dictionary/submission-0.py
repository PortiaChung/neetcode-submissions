class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        g = defaultdict(list)
        deg = defaultdict(int)
        for word in words:
            for c in word:
                deg[c] = 0
        
        for w1,w2 in pairwise(words):
            i=j = 0
            m,n = len(w1),len(w2)
            if m > n and w1.startswith(w2):
                return ""
            while i < m and j < n:
                if w1[i]!= w2[j]:
                    if w2[j] not in g[w1[i]]:
                        g[w1[i]].append(w2[j])
                        deg[w2[j]]+=1
                    break
                i+=1
                j+=1
        
        q = deque([c for c in deg if deg[c]==0])
        
        res = []
        cnt = 0
        while q:
            x = q.popleft()
            res.append(x)
            cnt+=1
            for y in g[x]:
                deg[y]-=1
                if deg[y] == 0:
                    q.append(y)
        return "".join(res) if cnt == len(deg) else ""


                    
        

