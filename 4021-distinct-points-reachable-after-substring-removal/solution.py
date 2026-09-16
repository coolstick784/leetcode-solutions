class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        res = set()
        left = 0
        cur_x = 0
        cur_y = 0
        right = 0
        if k >= len(s):
            return 1
        for idx, ch in enumerate(s):
            
            if ch == 'U':
                cur_y += 1
            elif ch == 'D':
                cur_y -= 1
            elif ch == 'L':
                cur_x -= 1
            else:
                cur_x += 1
        while right < len(s):
            goal = left + k
            while right < goal:
                ch = s[right]
                if ch == 'U':
                    cur_y -= 1
                elif ch == 'D':
                    cur_y += 1
                elif ch == 'L':
                    cur_x += 1
                else:
                    cur_x -= 1
                right += 1
            res.add((cur_x, cur_y))
            left += 1
            ch = s[left-1]
            if ch == 'U':
                cur_y += 1
            elif ch == 'D':
                cur_y -= 1
            elif ch == 'L':
                cur_x -= 1
            else:
                cur_x += 1



        return len(res)
