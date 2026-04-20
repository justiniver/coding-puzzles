class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        currLen = 0
        uniques = set()
        for i in range(len(s)):
            uniques.add(s[i])
            currLen += 1
            if (len(uniques) == currLen):
                maxLen = max(maxLen, currLen)
            else:
                print(f"{i}")
                while (len(uniques) < currLen):
                    uniques.discard(s[i - currLen + 1])
                    currLen -= 1

        return maxLen