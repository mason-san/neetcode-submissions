class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_stck = list() 
        speed_pos_arr = []
        n = len(position)

        #first build the array with speed and positions 
        for i in range(n): 
            speed_pos_arr.append({"position" : position[i], "speed" : speed[i]})
        
        #now we have something like 
        # [(1, 3), (4, 2)]
        # print(speed_pos_arr)
        #now i need to arrange this in decreasing order of positions 

        speed_pos_sorted_desc = sorted(speed_pos_arr, key=lambda x : x['position'], reverse=True)
        
        for each_car in speed_pos_sorted_desc:
            #calculate the time for each car 
            #time = (target - position) / speed 

            time = (target - each_car['position']) / each_car['speed']

            #if the time is equal or less then whats at the top of the fleet 
            if not fleet_stck or time > fleet_stck[-1]:
                fleet_stck.append(time)
        return len(fleet_stck)

        