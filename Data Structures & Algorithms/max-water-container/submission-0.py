class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_value = 0 

        #now i need to have two pointers 
        start = 0 
        end = len(heights) - 1

        #loop when start is smaller 
        while (start < end):
            #compute whatever water calcaultion 
            container_width = end - start 

            #water units 
            water_units_stored = container_width * min(heights[start], heights[end])

            max_value = max(max_value, water_units_stored)

            #now moving pointer logic 
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1

        return max_value 

        