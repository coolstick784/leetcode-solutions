class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        

        
        if len(tiles) == 1:
            return 1
        letters = set()
        res = 0
        for idx, ch in enumerate(tiles):
            if ch not in letters:
                letters.add(ch)
                res += 1 + self.numTilePossibilities(tiles[:idx] + tiles[idx+1:])
        return res

