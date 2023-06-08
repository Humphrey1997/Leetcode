#思路： 使用双指针,将高度较小的指针向另一个指针的方向移动

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # 计算当前容器的面积
            area = min(height[left], height[right]) * (right - left)
            
            # 更新最大面积
            max_area = max(max_area, area)
            
            # 移动较小的指针
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area