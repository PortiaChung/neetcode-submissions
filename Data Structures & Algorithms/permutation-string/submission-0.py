class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        if len(s1) > len(s2):
            return False
        
        cnt = defaultdict(int)
        for c in s1:
            cnt[c]+=1
        

        for i,c in enumerate(s2):
            cnt[c]-=1
            if cnt[c] == 0:
                del cnt[c]
            if i < len(s1)-1:
                continue
            if len(cnt)==0:
                return True
            out =s2[i-m+1]
            cnt[out] +=1
            if cnt[out] == 0:
                del cnt[out]    
        return False       


        