import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        for i in range(k):
            curr = heapq.heappop(nums)
            if i == k - 1:
                return -1 * curr
        