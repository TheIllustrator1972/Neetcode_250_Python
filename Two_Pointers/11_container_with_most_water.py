# Brute Force
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        for i in range(0, len(height)):
            for j in range(i + 1, len(height)):
                limitingHeight = min(height[i], height[j])
                currentVolume = limitingHeight * (j - i)
                if currentVolume > maxWater:
                    maxWater = currentVolume
        
        return maxWater

  # Two Pointer Approach
  class Solution:
    def maxArea(self, height: List[int]) -> int:
        l , r = 0, len(height) - 1
        maxWater = 0
        while l < r:
            currentVolume = min(height[l], height[r]) * (r - l)
            if currentVolume > maxWater:
                maxWater = currentVolume
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxWater
