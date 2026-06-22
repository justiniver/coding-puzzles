class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        tank = 0
        total = 0
        for i, gc in enumerate(zip(gas, cost)):
            g, c = gc
            total += g - c
            tank += g - c
            if tank < 0:
                start = i + 1
                tank = 0
        
        return start if total >= 0 else -1