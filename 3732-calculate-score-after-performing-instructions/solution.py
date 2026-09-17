class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        visited = set()
        i = 0
        res = 0
        while i >= 0 and i < len(values) and i not in visited:
            visited.add(i)
            ins = instructions[i]
            if ins == "add":
                res += values[i]
                i += 1
            else:
                i = i + values[i]
        return res
