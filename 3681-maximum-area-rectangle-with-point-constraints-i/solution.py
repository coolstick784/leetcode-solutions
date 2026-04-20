# for each point, ask if it can be a top left
# if it can, get the nearest one to the right
# then, get the nearest to the bottom
# then, ask if the right bottom is in our list of points to the bottom right
# then, ask if any points are in the rectangle

class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        res = -1
        x_dict = {}
        y_dict = {}


        # if any point is in between the y and x values (inclusive) and is not in our points, return False
        def is_valid(top_left, top_right, bottom_left, bottom_right):
            upper_y = top_left[1]
            left_x = top_left[0]
            right_x = bottom_right[0]
            lower_y = bottom_right[1]
            for x, y in points:
                if (x, y) in (top_left, top_right, bottom_left, bottom_right):
                    continue
                if x <= right_x and x >= left_x and y <= upper_y and y >= lower_y:
                    return False
            return True

  
        for x, y in points:
            x_dict.setdefault(x, []).append(y)
            y_dict.setdefault(y, []).append(x)
        for x in x_dict:
            x_dict[x].sort()
        for y in y_dict:
            y_dict[y].sort()
        for y in y_dict:
            if len(y_dict[y]) <= 1:
                continue
            cur_y = y
            for idx, cur_x in enumerate(y_dict[y][:-1]):
                top_left = (cur_x, cur_y)
                right_x = y_dict[cur_y][idx+1]
                top_right = (right_x, cur_y)
                
                if len(x_dict[cur_x]) <= 1:
                    continue
                x_idx =  x_dict[cur_x].index(cur_y) 
                if x_idx == 0:
                    continue
                bottom_y = x_dict[cur_x][x_idx-1]
                bottom_left = (cur_x, bottom_y)
                bottom_right = (right_x, bottom_y)
                if [right_x, bottom_y] in points and is_valid(top_left, top_right, bottom_left, bottom_right):
                    res = max(res, (
                        (cur_y-bottom_y)*(right_x-cur_x)
                    ))
                
                




        return res
