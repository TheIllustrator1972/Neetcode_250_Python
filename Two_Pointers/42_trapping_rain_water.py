# O(n) memory solution
class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        maxLeft = [0] * size
        maxRight = [0] * size

        minLeftAndRight = [0] * size

        leftMax = 0
        for i in range(0, size):
            if height[i] > leftMax:
                leftMax = height[i]
            maxLeft[i] = leftMax
        
        rightMax = 0
        for i in range(size - 1, -1, -1):
            if height[i] > rightMax:
                rightMax = height[i]
            maxRight[i] = rightMax

        ans = 0
        for i in range(0, size):
            minLeftAndRight[i] = min(maxLeft[i], maxRight[i])
            ans += minLeftAndRight[i] - height[i]

        return ans

# Two Pointer Approach
class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        l, r = 0, size - 1
        leftMax, rightMax = height[l], height[r]
        res = 0 
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else :
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
