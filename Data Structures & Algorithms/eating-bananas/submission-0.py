class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #minimum time to eat a pile of bananas 
        min_time = 1 

        #maximum time to eat a pile of bananas in piles
        max_time = max(piles)
        # max_time = 4

        #performing binary search
        # 1 < 25 (yes)
        min_speed_found = max(piles)
        while min_time <= max_time:

            k = (min_time + max_time) // 2
            # (2) / 2
            # k = 1

            #calcualte k for the middle value 
            #total hours for this k value
            total_hours = 0
            for i in range(len(piles)):
                total_hours += math.ceil(piles[i]/k)
            #total_hours = 10
            # 6 < 9
            if total_hours <= h:
                #max_time = 1
                min_speed_found = min(min_speed_found, k)
                max_time = k - 1
            # 10 > 4 (yes)
            else:
                #min_time = 1 + 1 = 2
                min_time = k + 1
        return min_speed_found