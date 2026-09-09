class Solution:
    def findMin(self, nums: List[int]) -> int:
        #lets get the left and right pointer 
        left = 0 
        right = len(nums) - 1

        # do the loop 
        while left < right:
            #take the mid element
            mid = (left + right) // 2

            #now i need to check if the mid element belongs to the left 
            # subsection or the right subsection

            if nums[mid] > nums[right]:
                left = mid + 1
            
            else: 
                right = mid
        
        #now the minimum element would be in the mid 
        return nums[left]

