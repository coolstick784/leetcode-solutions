class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = ["" for _ in range(numRows)]
        cur_row = 0
        dirn = "down"
        for idx, ch in enumerate(s):
            if dirn == "down" and cur_row < numRows:
                cur_row += 1
            elif dirn == "down" and cur_row == numRows:
                dirn = "up"
                cur_row -= 1
            elif dirn == "up" and cur_row > 1:
                cur_row -= 1
            elif dirn == "up" and cur_row == 1:
                dirn = "down"
                cur_row += 1
            print("cur row", cur_row, "ch", ch, "dir", dirn)
            rows[cur_row-1] += ch
        return "".join(rows)

        
