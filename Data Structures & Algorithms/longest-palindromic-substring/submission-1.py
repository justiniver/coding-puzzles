class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        
        def expandPalindrome(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            return l + 1, r - 1
        
        for i in range(len(s)):
            l1, r1 = expandPalindrome(i - 1, i + 1)
            l2, r2 = expandPalindrome(i, i + 1)
            l, r = (l1, r1) if r1 - l1 > r2 - l2 else (l2, r2)
            longest = longest if len(longest) >= r - l + 1 else s[l:r + 1]
        
        return longest
