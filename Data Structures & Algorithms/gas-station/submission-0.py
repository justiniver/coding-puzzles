class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [g - c for g, c in zip(gas, cost)]
        if sum(diff) < 0:
            return -1
        
        n = len(diff)
        skip_to = -1
        for i, d in enumerate(diff):
            if d < 0 or i < skip_to:
                continue
            tank = d
            i2 = i
            while tank >= 0:
                i2 += 1
                if i % n == i2 % n:
                    return i
                tank += diff[i2 % n]
            skip_to = i2