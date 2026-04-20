class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = dict()
        longest = 0
        currLen = 0
        for i in range(len(s)):
            freqMap[s[i]] = freqMap.get(s[i], 0) + 1
            currLen += 1
            if currLen - max(freqMap.values()) <= k:
                longest = max(longest, currLen)
            else:
                currLen -= 1
                freqMap[s[i - currLen]] = freqMap.get(s[i]) - 1
            
        return longest

        