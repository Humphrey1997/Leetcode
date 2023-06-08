#思路： 维护一个递增数组，但是运行太慢了

class Solution:
    def maxArea(self, height: List[int]) -> int:
        L = len(height)

        if height[0]>=height[1]:
            h_list = height[0:1]
            i_list = [0]
            pos = 0
        else:
            h_list = height[0:2]
            i_list = [0,1]
            pos = 1

        maxvol = min(height[0],height[1])

        for i in range(2,L):
            h = height[i]
            for j in range(pos+1):
                vol = (i - i_list[j])*min(h,h_list[j])
                maxvol = max(maxvol,vol)
                if h_list[j]>=h:
                    break

            if h>h_list[pos]:
                h_list.append(h)
                i_list.append(i)
                pos += 1

        return maxvol