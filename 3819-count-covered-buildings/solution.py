# at each x, we want to know the min and max y
# at each y, we want to know the min and max x
# for a point (x, y), if y is between the min and max for x, and x is between the min and max for y, it's covered

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:

        x_dict = {}
        y_dict = {}
        for x, y in buildings:
            x_dict[x] = x_dict.get(x, [float('inf'), -float('inf')])
            y_dict[y] = y_dict.get(y, [float('inf'),-float('inf')])
            x_dict[x][0] = min(x_dict[x][0], y)
            x_dict[x][1] = max(x_dict[x][1], y)
            y_dict[y][0] = min(y_dict[y][0], x)
            y_dict[y][1] = max(y_dict[y][1], x)
        res = 0
        for x, y in buildings:
            if x > y_dict[y][0] and x < y_dict[y][1] and y > x_dict[x][0] and y < x_dict[x][1]:
                res += 1
        return res
