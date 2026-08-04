class Solution:
    def minSwaps(self, s: str) -> int:
        ctr = Counter(s)
        if abs(ctr.get("1", 0) - ctr.get("0", 0)) > 1:
            return -1
        start_0 = 2000
        start_1 = 20000
        
        if ctr.get("1", 0) >= ctr.get("0", 0):
            start_1 = 0
            for idx, ch in enumerate(s):
                if idx % 2 == 0 and ch == "0":
                    start_1 += 1
        if ctr.get("0", 0) >= ctr.get("1", 0):
            start_0 = 0
            for idx, ch in enumerate(s):
                if idx % 2 == 0 and ch == "1":
                    start_0 += 1
        return min(start_0, start_1)

