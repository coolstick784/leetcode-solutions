class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = [[0 for _ in range(rows)] for _ in range(26)]
        self.letters = [chr(ch) for ch in range(ord('A'), ord('Z') + 1)]
        
    def charToInt(self, ch):
        return ord(ch) - ord('A')

    def setCell(self, cell: str, value: int) -> None:
        c = self.charToInt(cell[0])
        r = int(cell[1:])-1
        self.sheet[c][r] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        n1 = 0
        n2 = 0
        s1 = formula.split('+')[0][1:]
        s2 = formula.split('+')[1]
        if s1[0] in self.letters:
            
            n1 = self.sheet[self.charToInt(s1[0])][int(s1[1:])-1]
        else:
            n1 = int(s1)
        if s2[0] in self.letters:
            
            n2 = self.sheet[self.charToInt(s2[0])][int(s2[1:])-1]
        else:
            n2 = int(s2)
        
        return n1 + n2


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
