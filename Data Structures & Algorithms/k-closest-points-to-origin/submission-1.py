import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        out = []
        heap = []
        dist_map = defaultdict(list)
        for x, y in points:
            d = x**2 + y**2
            dist_map[d].append([x,  y])
            heapq.heappush(heap, d)
        
        while len(out) < k:
            small_d = heapq.heappop(heap)
            out.extend(dist_map[small_d])
        
        while len(out) > k:
            out.pop()
        
        return out
