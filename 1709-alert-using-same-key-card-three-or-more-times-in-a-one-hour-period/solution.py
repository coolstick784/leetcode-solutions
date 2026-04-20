# first, create a dictionary with each name, and each time they entered
# sort by time entered
# so we'll convert each time to an integer, as 60 * hour + minute
# then, for each time at the 3rd time or beyond, check if the past 2 times were within the past hour
# if they were, add it to the resoltuion
# otherwise, don't
# sort the final list 

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        names_dict = {}
        def cleanTime(t):
            hours = int(t[:2]) * 60
            return hours + int(t[3:])
        for idx, name in enumerate(keyName):
            time = cleanTime(keyTime[idx])
            names_dict.setdefault(name, []).append(time)
        for name in names_dict:
            names_dict[name].sort()
        res = []
        for name in names_dict:
            times = names_dict[name]
            if len(times) > 2:
                for idx, time in enumerate(times[2:]):
                    real_idx = idx + 2
                    if (time - times[real_idx-1] <= 60) and (time - times[real_idx-2] <= 60):
                        res.append(name)
                        break

        res.sort()
        return res
