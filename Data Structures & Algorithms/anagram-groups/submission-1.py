class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list) 
        for s in strs:
            cnt = [0]*26
            for c in s:
                cnt[ord(c) - ord("a")]+=1
            d[tuple(cnt)].append(s)
        return list(d.values())





        # d = defaultdict(list)
        # for s in strs:
        #     sorted_s = "".join(sorted(s))
        #     print(sorted_s)
        #     d[sorted_s].append(s)
        # return list(d.values())


        