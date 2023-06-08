# 思路：动态规划，对这种题不感兴趣，由gpt生成

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 创建动态规划数组，全部初始化为False
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # 初始条件：空模式可以匹配空字符串
        dp[0][0] = True
        
        # 处理空字符串与非空模式的情况
        for j in range(2, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
                
        # 填充动态规划数组
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 2]
        
        # 返回整个字符串是否匹配
        return dp[len(s)][len(p)]
