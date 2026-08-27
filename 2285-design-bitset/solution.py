class Bitset:

    def __init__(self, size: int):
        self.bits = [0 for _ in range(size)]
        self.flipped = False
        self.num_zero = size
        self.num_one = 0
        self.size = size

    def fix(self, idx: int) -> None:
        if (not self.flipped and self.bits[idx] == 0) or (self.flipped and self.bits[idx] == 1):
            self.num_zero -= 1
            self.num_one += 1
        if not self.flipped:
            self.bits[idx] = 1
        else:
            self.bits[idx] = 0


    def unfix(self, idx: int) -> None:
        if (self.flipped and self.bits[idx] == 0) or (not self.flipped and self.bits[idx] == 1):
            self.num_zero += 1
            self.num_one -= 1
        if not self.flipped:
            self.bits[idx] = 0
        else:
            self.bits[idx] = 1

    def flip(self) -> None:
        self.flipped = not self.flipped
        self.num_zero, self.num_one = self.num_one, self.num_zero
        

    def all(self) -> bool:
        return self.num_one == self.size
        

    def one(self) -> bool:
        return self.num_zero != self.size
        

    def count(self) -> int:
        
        return self.num_one
        

    def toString(self) -> str:
        if not self.flipped:
            return "".join(str(n) for n in self.bits)
        return "".join(str(-n+1) for n in self.bits)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
