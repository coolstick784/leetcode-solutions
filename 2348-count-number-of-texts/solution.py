class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        map_dict = {
            "2":["a", "b", "c"],
            "3":["d", "e", "f"],
            "4":["g", "h", "i"],
            "5":["j", "k", "l"],
            "6":["m", "n", "o"],
            "7":["p", "q", "r", "s"],
            "8":["t", "u", "v"],
            "9":["w", "x", "y", "z"]
        }

        @lru_cache(None)
        def solve(idx): # we can either press it 1, 2, 3, or 4 times
            if idx == len(pressedKeys):
                return 1
            if idx > len(pressedKeys):
                return 0
            ch = pressedKeys[idx]
            out = []
            
            poss = len(map_dict[ch])
            ctr = 1
            cur = idx
            while ctr <= poss and cur < len(pressedKeys) and pressedKeys[cur] == ch:
                out.append(solve(cur+1))
                cur += 1
                ctr += 1

            return sum(out) % (10**9+7)


        

        return solve(0)
