class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # 1. Get the number closest to the average
        # 2. Get the distances from each other number to that number
        # 3. Return the result
        full = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                full.append(grid[r][c])
        mean_val = sum(full)/len(full)
        print("mean", mean_val)
        
        min_distance_neg = -2**31
        min_distance_pos = 2**31-1
        min_val = -1
        min_higher_val = -1
        avg_value = -1
       
        full.sort()
        if len(full) % 2 ==0:
            poss = [full[len(full) // 2], full[len(full) // 2 -1]]
        else:
            poss = [full[len(full) // 2]]
            
        
        
        res = 2**31-1

        for avg_value in poss:

            cur_res = 0
            for n in full:
                cur_res += abs(int(n - avg_value) / int(x))
                if (n-avg_value) % x != 0:
                    return -1
            print(avg_value)
            print("cur res", cur_res)

            res = min(cur_res, res)

        return int(res) 


