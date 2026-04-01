class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        # If the sum of the col is 0, both are  0
        # If the sum is 2, both are 1
        # Have the rest be -1 
        # If the remaining sum of upper is u and the remaining sum of lower is l, fill in the first u columns in upper with u and the lower ones with l
        # If we run our of upper or lower fields, return []
        
        cur_upper = 0
        cur_lower = 0
        u_row = [-1 for _ in range(len(colsum))]
        l_row = [-1 for _ in range(len(colsum))]
        for idx, c in enumerate(colsum):
            if c == 2:
                u_row[idx] = 1
                cur_upper += 1
                l_row[idx] = 1
                cur_lower += 1
            elif c == 0:
                u_row[idx] = 0
                l_row[idx] = 0
        diff_upper = upper - cur_upper
        diff_lower = lower - cur_lower
        idx = 0
        if diff_upper < 0 or diff_lower < 0:
            return []
        while diff_upper > 0:
            if idx >= len(u_row):
                return []
            c = u_row[idx]
            if c == -1:
                u_row[idx] = 1
                l_row[idx] = 0
                diff_upper -= 1
            idx += 1

    
        idx = 0
    
        while diff_lower > 0:
            if idx >= len(u_row):
                return []
            c = l_row[idx]
            if c == -1:
                l_row[idx] = 1
                u_row[idx] = 0
                diff_lower -= 1
            idx += 1

 
        if -1 in u_row or -1 in l_row:
            return []
        return [u_row, l_row]


        
