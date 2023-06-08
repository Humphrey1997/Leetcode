# 思路：从中间向两边找，分奇偶两种情况讨论
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen = 1
        pos = 0
        N = len(s)
        for i in range(N):
            nowlen1 = 1
            nowlen2 = 1
            j = 1
            while i-j>=0 and i+j<N and s[i-j]==s[i+j]:
                nowlen1 = 2*j+1
                j += 1
            j = 1
            while i-j>=0 and i+j-1<N and s[i-j]==s[i+j-1]:
                nowlen2 = 2*j
                j += 1
            nowlen = max(nowlen1,nowlen2)
            if nowlen>maxlen:
                maxlen = nowlen
                pos = i-nowlen//2
        return s[pos:pos+maxlen]