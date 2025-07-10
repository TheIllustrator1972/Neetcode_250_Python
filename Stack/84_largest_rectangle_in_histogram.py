# Brute Force
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        for i in range(len(heights)):
            for j in range(i, len(heights)):
                maxArea = max(maxArea, (j - i + 1) * min(heights[i:j + 1]))
        
        return maxArea

# Stack Approach
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair: (index, height)
        # if heights are in increasing order simply add to stack (move the current rectangle forward), 
        # if current height is less than what's top on stack, 
        # then pop and try to extend the current rectangle backward

        for i, h in enumerate(heights):
            start = i
            # height on top of stack
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            
            stack.append((start, h))

        # Some elements can be remaining in the stack, whose rectangles will strech till th end of histogram
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea
        
        return maxArea
