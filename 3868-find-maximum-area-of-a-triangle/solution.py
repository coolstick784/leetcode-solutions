# we want to know the highest x,  lowest x, highest y, and lowest y
# for each x value, get the highest and lowest y for that x
# then, multiply the difference between that differnece ebtween lowest x/highest x vs current x
# for each y value, get the highest and lowest x for that y
# then, multiply the difference between that differnece ebtween lowest y/highest y vs current y


class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        x_dict = {} # for each x, [min_y, max_y]
        y_dict = {} # for each y, {min_x, max_x}
        min_x = float('inf')
        max_x = -float('inf')
        max_y = -float('inf')
        min_y = float('inf')
        for x, y in coords:
            cur_x_min, cur_x_max = x_dict.get(x, [float('inf'), -float('inf')])
            cur_y_min, cur_y_max = y_dict.get(y, [float('inf'), -float('inf')])
            x_dict[x] = [min(y, cur_x_min), max(y, cur_x_max)]
            y_dict[y] = [min(x, cur_y_min), max(x, cur_y_max)]
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)
        res = -1
        for x in x_dict:
            y_diff = x_dict[x][1] - x_dict[x][0]
            height = max(x - min_x, max_x - x)

            if y_diff > 0 and height > 0:
                res = max(res, y_diff * height)

        for y in y_dict:
            x_diff = y_dict[y][1] - y_dict[y][0]
            height = max(y - min_y, max_y - y)

            if x_diff > 0 and height > 0:
                res = max(res, x_diff * height)
        return res




        
