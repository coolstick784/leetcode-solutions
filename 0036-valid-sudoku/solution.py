class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in board:
            non_empty = [c for c in r if c != "."]
            print(non_empty)
            if len(non_empty) != len(list(set(non_empty))):
                print("rows bad")
                return False
        cols = [[] for _ in range(9)]
        for r in board:
            for idx,c in enumerate(r):
                cols[idx].append(c)
        for col in cols:
            non_empty = [c for c in col if c != "."]
            if len(non_empty) != len(list(set(non_empty))):
                print("cols bad")
                return False
        boxes = [[] for _ in range(9)]
        #0,0 -> 0 0, 4 -> 1 0, 7 -> 2
        # 3, 1 -> 3

        for rnum, r in enumerate(board):
            for cnum, c in enumerate(r):
                multiplier = 3 * (rnum // 3)
                adder = cnum // 3
                boxes[multiplier + adder].append(c)
        for b in boxes:
            non_empty = [c for c in b if c != "."]
            if len(non_empty) != len(list(set(non_empty))):
                print("boxes bad")
                return False
        return True
