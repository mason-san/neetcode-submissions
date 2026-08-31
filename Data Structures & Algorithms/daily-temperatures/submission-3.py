class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #The stack should store indices. 
        stack = list()
        res = [0] * len(temperatures)

        stack.append(0)
        
        #loop through the temperatures
        for i in range(1, len(temperatures)):

            # check if its greater 
            while stack and temperatures[i] > temperatures[stack[-1]]:
                element = stack.pop()
                res[element] = i - element
            stack.append(i)
        return res

