from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cnt = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            cnt[sorted_s].append(s)
        return list(cnt.values())

        