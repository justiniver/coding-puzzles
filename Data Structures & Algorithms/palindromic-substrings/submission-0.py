class Solution:
    def countSubstrings(self, s: str) -> int:
        out = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                out += 1
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                out += 1
                l -= 1
                r += 1
        
        return out