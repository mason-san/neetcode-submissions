class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        #Iterating through the array 
        #let's have a left and right pointer
        left = 0 
        right = len(height) - 1

        #let's build prefix array first
        for i in range(1, len(height)):
            prefix[i] = max(prefix[i - 1], height[i - 1])
        
        # now let's build suffix array 
        for j in range(len(height) - 2, -1, -1):
            suffix[j] = max(suffix[j + 1], height[j + 1])

        total_water_capacity = 0 
        for i in range(len(height)):
            water_at_idx = min(prefix[i], suffix[i]) - height[i]

            if (water_at_idx > 0):
                total_water_capacity += water_at_idx

        return total_water_capacity
