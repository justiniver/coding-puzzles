class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True
        n = len(hand)
        if n % groupSize != 0:
            return False
        freq = dict()
        for h in hand:
            freq[h] = freq.get(h, 0) + 1
        heapq.heapify(hand)
        for _ in range(n // groupSize):
            start = heapq.heappop(hand)
            while freq[start] == 0:
                start = heapq.heappop(hand)
            for i in range(start, start + groupSize):
                if i not in freq or freq[i] == 0:
                    return False
                freq[i] -= 1
        
        return True