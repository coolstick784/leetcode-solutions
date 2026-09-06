class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a = 0
        b = 0
        for idx, ch in enumerate(colors):
            if idx > 0 and idx < len(colors) - 1 and ch == colors[idx-1] and ch == colors[idx+1]:
                if ch == 'A':
                    a += 1
                else:
                    b += 1
        return a > b
