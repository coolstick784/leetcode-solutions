class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # list of directions
        # right -> down -> left -> up
        # if you've hit an element you've already hit, or are out of space go to the next direction
        
        res = [[None for _ in range(n)] for _ in range(n)]
        dins = ['right', 'down', 'left', 'up']
        dir_n = 0
        ctr = 1
        cur_el = (0, 0)
        explored = set()
        max_val = n*n
        
        def get_next_el(cur_el, dir_n):
            cur_dir = dins[dir_n]

            if cur_dir == 'right':
                next_poss = (cur_el[0], cur_el[1]+1)
            elif cur_dir == 'down':
                 next_poss = (cur_el[0]+1, cur_el[1])
            elif cur_dir == 'left':
                next_poss = (cur_el[0], cur_el[1]-1)
            elif cur_dir == 'up':
                 next_poss = (cur_el[0]-1, cur_el[1])
            if next_poss in explored or next_poss[0] < 0 or next_poss[0] >= n or next_poss[1] < 0 or next_poss[1] >= n:
                dir_n = (dir_n + 1) % 4
                return get_next_el(cur_el, dir_n)

            
            
            explored.add(next_poss)
            return [next_poss, dir_n]
        while ctr < max_val:
            
            cur_r = cur_el[0]
            cur_c = cur_el[1]
            explored.add((cur_r, cur_c))
            res[cur_r][cur_c] = ctr
            cur_el, dir_n = get_next_el(cur_el, dir_n)
            
            
            
            ctr += 1
        cur_r = cur_el[0]
        cur_c = cur_el[1]
        explored.add((cur_r, cur_c))
        res[cur_r][cur_c] = ctr
        return res
            
