class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = {}
        balls = {}
        res = []
        all_colors = set()

        for ball, color in queries:
            if ball in balls:
                prev = balls[ball]
                colors[prev] -= 1
                if colors[prev] == 0:
                    all_colors.remove(prev)

            balls[ball] = color
            colors[color] = colors.get(color, 0) + 1
            all_colors.add(color)

            res.append(len(all_colors))

        return res
