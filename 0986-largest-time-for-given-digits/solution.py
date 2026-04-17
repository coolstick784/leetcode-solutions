# get all possible hour and minute combos, turn those into 4 digit numbers, then get the max and convert to str

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        total = permutations(arr)
        possible = []
        for p in total:
            if (p[0] <= 1 or (p[0] ==2 and p[1] < 4)) and p[2] < 6:
                possible.append(p)
        print(possible)
        res = -1
        for p in possible:
            res = max(res, 
                int(
                    "".join([str(d) for d in p])
                )
           )
        if res == -1:
            return ""
        res = str(res)
        while len(res) < 4:
            res = "0" + res
        res = res[:2] + ":" + res[2:]
        return res
            
        
