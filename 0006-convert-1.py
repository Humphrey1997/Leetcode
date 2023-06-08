# 思路：按规则排列，然后输出
# 二维数组占用空间太大了，用numRows个字符串最后拼起来就行
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        N = len(s)
        M = numRows
        res = ""
        str_array = [[False for j in range(N)] for i in range(M)]

        k = 0
        i = 0
        j = 0
        flag = 1
        while k<N:
            print(i,j)
            str_array[i][j] = s[k]
            k += 1
            if M == 1:
                j += 1
            else:
                if flag == 1:
                    i += 1
                else:
                    i -= 1
                    j += 1
                if i == M-1:
                    flag = 2
                elif i==0:
                    flag = 1

        for i in range(M):
            for j in range(N):
                if str_array[i][j]:
                    res += str_array[i][j]
        return res