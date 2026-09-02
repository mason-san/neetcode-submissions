class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #two stacks for left and for righty 
        stack = []
        left_boundary = [-1] * len(heights)
        #let's first go through the heights bars 
        for i in range(len(heights)):

            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                left_boundary[i] = stack[-1]

            stack.append(i)
        
        #right boundary list 
        right_boundary = [len(heights)] * len(heights)
        stack = []

        #going from right to left
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack: 
                right_boundary[i] = stack[-1]
            
            stack.append(i)

        area = 0 
        for i in range(len(heights)):
            width = (right_boundary[i] - left_boundary[i]) - 1

            area = max(area, (heights[i] * width))
        return area
