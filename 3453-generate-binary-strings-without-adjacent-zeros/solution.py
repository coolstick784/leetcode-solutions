class Solution:
    def validStrings(self, n: int) -> List[str]:
        def solve(num):
            if num == 1:
                return ["0", "1"]
            res = []
            for sol in solve(num-1):
                if sol[-1] == "1":
                    res.append(sol + "0")
                res.append(sol + "1")
            return res

        return solve(n)
