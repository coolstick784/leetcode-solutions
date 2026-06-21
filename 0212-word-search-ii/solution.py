class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        pre = {}
        res = set()
        for word in words:
            cur = pre
            for idx, ch in enumerate(word):
                cur.setdefault(ch, {})
                cur = cur[ch]
                if idx == len(word) - 1:
                    cur[True] = word
        def explore(r, c, cur, explored):
            if True in cur:
                res.add(cur[True])
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or (r, c) in explored or not cur:
                return
            ch = board[r][c]
          
            explored.add((r, c))
            nxt = cur.get(ch, set())
            if nxt:
                explore(r, c+1, nxt, explored)
                explore(r, c-1, nxt, explored)
                explore(r+1, c, nxt, explored)
                explore(r-1, c, nxt, explored)
            explored.remove((r, c))


        for r, row in enumerate(board):
            for c, el in enumerate(row):
                explore(r, c, pre, set())
        return list(res)

