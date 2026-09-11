class TimeMap:
    # res = {}
    #i think the dictionary could look something like 
    #{("alice", 3) : "happy"}
    def __init__(self):
        #i have to use a dictionary.
        self.res = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        value_paired = [value, timestamp]

        if key in self.res.keys():
            self.res[key].append(value_paired) 
        else:
            self.res[key] = [value_paired]

    def get(self, key: str, timestamp: int) -> str:
        #Get the value list 
        if key in self.res.keys():
            values = self.res[key]
        else:
            return ""

        #build a list of timestamps 
        # timestamps = []

        # for value in values:
        #     timestamps.append(value[1])

        #Now perform binary search 

        l = 0 
        r = len(values) - 1
        best_index = -1

        while l <= r:
            mid = (l + r) // 2

            if values[mid][1] <= timestamp:
                best_index = mid
                l = mid + 1

            else:
                r = mid - 1

        if best_index == -1:
            return ""
        return values[best_index][0]