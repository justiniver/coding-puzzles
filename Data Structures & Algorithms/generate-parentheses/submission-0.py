class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        valid = []
        
        def buildValidParensFromOpenAndCloseCounts(numOpen, numClose):
            if numOpen == n and numClose == n:
                out.append("".join(valid))
                return

            if numOpen < n:
                valid.append("(")
                buildValidParensFromOpenAndCloseCounts(numOpen + 1, numClose)
                valid.pop()
            
            if numOpen > numClose:
                valid.append(")")
                buildValidParensFromOpenAndCloseCounts(numOpen, numClose + 1)
                valid.pop()
        
        buildValidParensFromOpenAndCloseCounts(0, 0)
        return out