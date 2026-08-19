class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0

        for n in numbers: 
            seq = 1
            if n - 1 in numbers: 
                continue 
            
            #the number is the beginning 
            #check sequence 
            tmp = n
            while(tmp + 1 in numbers):
                tmp = tmp + 1
                seq += 1
            
            longest = max(longest, seq)

        print(longest)
        
        # print(seq)
        return longest


        