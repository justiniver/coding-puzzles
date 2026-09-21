class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # idea is that we have some dp where dp[i][j][k] represents
        # whether we can create s3[:k] using s1[:i] and s2[:j].
        # We want to "flatten" this idea from 3D to 2D, so we can
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if (i, j) == (0, 0):
                    dp[i][j] = True
                    continue
                t = s3[i + j - 1]
                if ((dp[i - 1][j] and s1[i - 1] == t) or
                    (dp[i][j - 1] and s2[j - 1] == t)):
                    dp[i][j] = True
        
        return dp[-1][-1]