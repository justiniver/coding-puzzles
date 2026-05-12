class Solution:
    # this is fine but there is also a pretty cool solution where you pass in l, r to the isPalindrome helper directly
    # and that way you can avoid string splicing.
    def partition(self, s: str) -> List[List[str]]:
        out = []
        valid = []
        def _isPalindrome(s) -> bool:
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def buildValidSubstringsFromIdx(currIdx: int):
            if currIdx >= len(s):
                out.append(valid.copy())
                return
            
            for i in range(currIdx, len(s)):
                currSS = s[currIdx:i + 1]
                if _isPalindrome(currSS):
                    valid.append(currSS)
                    buildValidSubstringsFromIdx(i + 1)
                    valid.pop()
            
        buildValidSubstringsFromIdx(0)
        return out

        