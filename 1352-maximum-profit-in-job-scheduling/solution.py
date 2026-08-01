
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        data = list(zip(startTime, endTime, profit))
        data.sort()
        best_idxs = []
        best_vals = []
        res = 0

        def findVal(s):
            left = 0
            right = len(best_idxs) - 1
            if s > best_idxs[0]:
                return 0
            
            while left < right:
                med = (left + right) // 2
                if best_idxs[med] == s or (best_idxs[med] > s and best_idxs[med+1] < s):
                    return best_vals[med]
                elif best_idxs[med] > s:
                    left = med + 1
                else:
                    right = med
            return best_vals[left]
        for idx in range(len(data) -1, -1, -1):
            start, end, p = data[idx]
            if best_idxs:
                val = findVal(end) + p
                if val > best_vals[-1]:
                    while best_idxs and start == best_idxs[-1]:
                        best_idxs.pop()
                        best_vals.pop()
                    best_idxs.append(start)
                    best_vals.append(val)
                    res = max(res, val)
            
            else:
                best_idxs.append(start)
                best_vals.append(p)
                res = max(res, p)

        print(data)
        print(best_idxs)
        print(best_vals)
        return res
