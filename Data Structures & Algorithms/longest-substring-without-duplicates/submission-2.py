class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        currLen = 0
        uniques = set()
        for i in range(len(s)):
            if s[i] in uniques:
                while s[i] in uniques:
                    uniques.discard(s[i - currLen + 1])
                    currLen -= 1
            uniques.add(s[i])
            currLen += 1
            maxLen = max(maxLen, currLen)
        return maxLen