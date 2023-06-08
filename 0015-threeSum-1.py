# 思路：将数组排序，使用双指针进行查找,注意去重

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 排序数组
        result = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:  # 避免重复的第一个数
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                
                if sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # 跳过重复的左指针和右指针
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return result
