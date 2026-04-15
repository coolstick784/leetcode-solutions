
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sums = set([0])
        for s in stones:
            new_sums = set()
            for su in sums:
                new_sums.add(abs(su-s))
                new_sums.add(abs(su+s))
            sums = new_sums.copy()
        return min([abs(s) for s in sums])

        

        

