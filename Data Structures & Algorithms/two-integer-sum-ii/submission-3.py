class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #perform binary search? 
        #so get the mid element 
        start = 0
        end = len(numbers) - 1

        ans = []

        #now 
        while (start < end):
            #Get the middle value 

            
            #now i just need to add both start and end 
            if numbers[start] + numbers[end] > target:
                end -= 1
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                ans.append(start+1)
                ans.append(end + 1)
                end -= 1

        return ans

        