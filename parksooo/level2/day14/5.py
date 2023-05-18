class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        dp = [[0 for i in range(s_len)] for j in range(s_len + 1)]
        maxlen = 0
        res = ""
        for i in range(s_len):
            for j in range(i, s_len):
                if i == 0:
                    dp[i + 1][j] = 1
                else :
                    if dp[i - 1][j - 1] >= 0 and s[j] == s[j - i]:
                        dp[i + 1][j] = dp[i - 1][j - 1] + 2
                    else :
                        dp[i + 1][j] = -1
                
                if dp[i + 1][j] > maxlen:
                    maxlen = dp[i + 1][j]
                    res = s[j - i : j + 1]
        return res

test = Solution()
print(test.longestPalindrome("cddb"))