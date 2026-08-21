class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = defaultdict(int)
        for c in t:
            cnt[c]+=1
        
        need = len(cnt)
        l = 0
        resl,resr = -1,len(s)
        for r,c in enumerate(s):
            cnt[c]-=1
            if cnt[c] == 0:
                need -=1
            
            while need == 0:
                if r-l < resr-resl:
                    resl,resr = l,r
                
                if cnt[s[l]] == 0:
                    need +=1
                cnt[s[l]]+=1
                l+=1
        return "" if resl < 0 else s[resl:resr+1]

        