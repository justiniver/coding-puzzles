class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [-1] * n, [n] * n
        sl, sr = [], []

        for i in range(n):
            j = n - 1 - i

            while sl and heights[sl[-1]] >= heights[i]:
                sl.pop()
            while sr and heights[sr[-1]] >= heights[j]:
                sr.pop()

            if sl: left[i] = sl[-1]
            if sr: right[j] = sr[-1]

            sl.append(i)
            sr.append(j)

        return max(
            h * (right[i] - left[i] - 1)
            for i, h in enumerate(heights)
        )