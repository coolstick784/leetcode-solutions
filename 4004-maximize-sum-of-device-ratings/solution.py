# find the device with the lowest 2nd lowest unit
# move all of the lowest units to that unit
# get the 2nd lowest from each

class Solution:
    def maxRatings(self, units: List[List[int]]) -> int:
        lowest = min([unit for device in units for unit in device])
        second_lowest = []
        for device in units:
            device.sort()
            if len(device) >= 2:
                second_lowest.append(device[1])
            else:
                second_lowest.append(device[0])
        s = sum(second_lowest) - min(second_lowest)
        s += lowest
        return s
