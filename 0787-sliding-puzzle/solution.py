class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        explored = []
        def swap(b, r, c, nr, nc, pts):
            if nr < 0 or nc < 0 or nr >= 2 or nc >= 3:
                return 
            new = [[n for n in r] for r in b]
          
            new[r][c], new[nr][nc] = new[nr][nc], new[r][c]

            
            q.append((new, pts+1))
        q = deque([(board, 0)])
        while q:
          
            cur, pts = q.popleft()
      
            
          

            if not cur or cur in explored:
                continue
            if cur == [[1, 2, 3], [4, 5, 0]]:
                return pts
            explored.append(cur)
            boards = []
            if 0 in cur[0]:
                r = 0
                c = cur[0].index(0)
            else:
                r = 1
                c = cur[1].index(0)
        
            swap(cur, r, c, r-1, c, pts)

            
            swap(cur, r, c, r+1, c, pts)
            swap(cur, r, c, r, c+1, pts)
            swap(cur, r, c, r, c-1, pts)
      
     



 
        return -1 
