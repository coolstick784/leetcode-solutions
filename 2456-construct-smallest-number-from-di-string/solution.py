# we ask what the smallest possible number is given what we've already used, and the index we're at

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        

        def solve(used, idx):
            set_used = set(used)
            for n in range(1, 10):
                if n not in set_used:
                    if pattern[idx] == "I" and n <= used[-1]:
                        return [False, []]
                    if pattern[idx] == "D" and n >= used[-1]:
                        return [False, []]
                    if idx == len(pattern) - 1:
                        return [True, used + [n]]
                    
                    can_be_done, out = solve(used + [n], idx+1)
                    if can_be_done:
                        return [True, out]

        for n in range(1, 10):
            is_possible, res = solve([n], 0)
            if is_possible:
                return "".join([str(n) for n in res])
