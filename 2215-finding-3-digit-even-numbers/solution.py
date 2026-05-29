class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        out = set()
        for idx, d in enumerate(digits):
            if  d == 0:
                continue
            for idx2, d2 in enumerate(digits):
                if idx2 == idx:
                    continue
                for idx3, d3 in enumerate(digits):
                    if idx2 == idx3 or idx3 == idx:
                        continue
                    if d3 % 2 != 0:
                        continue
                    out.add(d3 + d2*10 + d * 100)
        return sorted(list(out))
