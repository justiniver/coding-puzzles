import heapq
from collections import defaultdict

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        out = []
        heap = []
        dist_map = defaultdict(list)
        for x, y in points:
            d = x**2 + y**2
            if d not in dist_map:
                heapq.heappush(heap, d)
            dist_map[d].append([x,  y])
        
        while len(out) < k:
            small_d = heapq.heappop(heap)
            out.extend(dist_map[small_d])
        
        while len(out) > k:
            out.pop()
        
        return out