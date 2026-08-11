class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cnt = Counter(hand)
        hand.sort()
        for x in hand:
            if cnt[x] == 0:
                continue
            for i in range(groupSize):
                y = x+i
                if cnt[y] > 0:
                    cnt[y]-=1
                else:
                    return False
        return True
        