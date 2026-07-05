from collections import deque
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        best = {} # (r, c): num, count


        possible = False
        explored = set()
        explored.add((len(board)-1, len(board[0])-1))
        q = deque(
            [(len(board)-1, len(board[0])-1)]
        )
        while q:
      
            r, c = q.popleft()
        
            if r == 0 and c == 0:
                possible = True
                break

            if r < 0 or c < 0:
                continue
            if board[r][c] == 'X':
                continue
            if (r-1, c-1) not in explored:
                q.append((r-1, c-1))
                explored.add((r-1, c-1))
            if (r-1, c) not in explored:
                q.append((r-1, c))
                explored.add((r-1, c))
            if (r, c-1) not in explored:
                q.append((r, c-1))
                explored.add((r, c-1))
            
        if not possible:
            return [0, 0]


        nums = set([str(i) for i in range(10)])
        for r in range(len(board)-1, -1, -1):
            for c in range(len(board[0])-1, -1, -1):
                
                el = board[r][c]

                if el == 'X' or (r, c) not in explored:
                    best[(r, c)] = [0, 0]
                    continue
                if el in nums:
                    el = int(el)
                else:
                    el = 0
                best_dr = best.get((r+1, c+1), [0, 0])
                best_down = best.get((r+1, c), [0, 0])
                best_right = best.get((r, c+1), [0, 0])
                
                mx = max(best_dr[0], best_down[0], best_right[0])


                ct = 0
                if best_dr[0] == mx:
                    ct +=  best_dr[1]
                if best_down[0] == mx:
                    ct += best_down[1]
                if best_right[0] == mx:
                    ct += best_right[1]
                ct = max(1, ct)
                ct = ct % (10**9+7)
                best[(r, c)] = [el+mx, ct]

        print(best)
        return best[(0,0)]
