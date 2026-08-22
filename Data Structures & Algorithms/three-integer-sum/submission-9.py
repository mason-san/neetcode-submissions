class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #lets first sort numbers 
        nums_sorted = sorted(nums)
        ans = list()

        #now we have 
        #[0, 1, 1]
        #or for [-1, 0, 1, 2, -1, -4]
        #we have [-4, -1, -1, 0, 1, 2]

        #what do you do to this? 
        #let's loop through the nums 

        for i in range(len(nums_sorted)):
            #if the values are positive, just skip it 
            if (nums_sorted[i] > 0):
                break

            #if the values are the same, then why bother doing a search again 
            if i > 0 and nums_sorted[i] == nums_sorted[i - 1]:
                continue

            # now i'm at the first 
            j = i + 1
            k = len(nums_sorted) - 1

            # print(k)

            #j is at left and k is at right
            while (j < k):
                target = -(nums_sorted[i])

                if (nums_sorted[j] + nums_sorted[k] < target):
                    j += 1
                
                elif (nums_sorted[j] + nums_sorted[k] > target):
                    k -= 1
                
                else:
                    ans.append([nums_sorted[i], nums_sorted[j], nums_sorted[k]])
                    # print(ans)
                    current_left_pointer = nums_sorted[j]
                    current_right_pointer = nums_sorted[k]

                    #updating left and right
                    j += 1
                    k -= 1

                    while(j < k and nums_sorted[j] == current_left_pointer):
                        j += 1
                    while(j < k and nums_sorted[k] == current_right_pointer):
                        k -= 1
            
        return ans
        