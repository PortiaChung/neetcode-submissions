class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        m,n = len(s1), len(s2)
        if len(s1) > len(s2):
            return False
        
        cnt = defaultdict(int)
        for c in s1:
            cnt[c]+=1
        
        left = 0
        for i,c in enumerate(s2):
            cnt[c]-=1
            if cnt[c] == 0:
                del cnt[c]
            left = i-m+1
            if  left < 0:
                continue
            if len(cnt) == 0:
                return True
            
            cnt[s2[left]]+=1
            if cnt[s2[left]] == 0:
                del cnt[s2[left]]
        return False
            



        

       