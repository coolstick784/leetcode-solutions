# its inclusive
class RLEIterator:

    def __init__(self, encoding: List[int]):
        idx = 0
        self.encoding = encoding
        cur_start = 0
        cur_end = 0
        self.arr = []
        while idx < len(self.encoding):
            if self.encoding[idx] == 0:
                idx += 2
                continue
            n = self.encoding[idx+1]
            cur_end = cur_start + self.encoding[idx] - 1

            self.arr.append((cur_start, cur_end, n))
            cur_start = cur_end + 1
            idx += 2
        self.cur_idx_arr = 0 # cur index in self.arr
        self.cur_exp = 0 # cur index if self.arr was expanded
        

    def next(self, n: int) -> int:
        if self.cur_idx_arr >= len(self.arr):
            return -1
        cur_start, cur_end, cur_n = self.arr[self.cur_idx_arr]
        self.cur_exp += n # return the value at n-1
        
        while self.cur_exp > cur_end :
   
            self.cur_idx_arr += 1
            if self.cur_idx_arr >= len(self.arr):
                if self.cur_exp > self.arr[-1][1] + 1:
                    return -1
                else:
                    return self.arr[-1][2]
            cur_start, cur_end, cur_n = self.arr[self.cur_idx_arr]
        if self.cur_exp-1 >= cur_start:
            return cur_n
        else:
            return self.arr[self.cur_idx_arr-1][2]
        

        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
