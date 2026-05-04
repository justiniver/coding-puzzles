class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) <= 1:
            return 0 if not stones else stones[0]
        stones.sort(reverse=True)
        if stones[0] == stones[1]:
            return self.lastStoneWeight(stones[2:])
        else:
            return self.lastStoneWeight(stones[2:] + [abs(stones[0] - stones[1])])