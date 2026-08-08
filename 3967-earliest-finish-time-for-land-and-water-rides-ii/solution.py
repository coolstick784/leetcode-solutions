# for each time t, what's the latest we can start a land ride, and what's the earliest we can end a water ride?

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        earliestLandEnd = min([t + d for t, d in list(zip(landStartTime, landDuration))])
        earliestWaterEnd = min([t + d for t, d in list(zip(waterStartTime, waterDuration))])
        land_heap = []
        water_heap = []
        
        land = [(t+d, t, d) for t, d in list(zip(landStartTime, landDuration))]
        land.sort()
        water = [(t+d, t, d) for t, d in list(zip(waterStartTime, waterDuration))]
        water.sort()
        min_land_dist = float('inf')
        min_water_dist = float('inf')
        land_idx = -1
        water_idx = -1

        t = 0
        while True:
            t += 1
            while land_idx+1 < len(land) and land[land_idx+1][0] <= t:
                land_idx += 1
                min_land_dist = min(min_land_dist, land[land_idx][2])
            if earliestWaterEnd <= t - min_land_dist:
                return t
            while water_idx + 1 < len(water) and water[water_idx+1][0] <= t:
                water_idx += 1
                min_water_dist = min(min_water_dist, water[water_idx][2])
            if earliestLandEnd <= t - min_water_dist:
                return t
