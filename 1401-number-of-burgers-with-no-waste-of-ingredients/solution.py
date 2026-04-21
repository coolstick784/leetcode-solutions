class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        # j + s = cheeeseSlices
        # 4j + 2s = tomatoSlices
        # 2j = tomatoSlices - 2 * cheeseSlices

        j = (tomatoSlices - 2 * cheeseSlices) /2
        s = cheeseSlices - j
        if float(j) == float(int(j)) and j >= 0 and s >= 0:
            return [int(j), int(s)]
        return []

