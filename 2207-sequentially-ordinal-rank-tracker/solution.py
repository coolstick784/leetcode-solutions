# have a descending heap of the top yet to be popped and an ascending heap of what has been popped
# when we call add, add to the ascending then pop from ascending and add to descending
# when we call get, get the first from descending

import heapq
class SORTracker:

    def __init__(self):
        self.ascending = []
        self.descending = []
        self.ctr = 0
    def rev_name(self, name):

        return "".join([chr(ord('a') + ord('z') - ord(ch)) for ch in name])

    def clean_name(self, name):
        pad_l = 11 - len(name)
        return name + pad_l * chr(ord('a') - 1)
        

    def add(self, name: str, score: int) -> None:
   
        name = self.clean_name(name)
        heapq.heappush(self.ascending, (score, self.rev_name(name)))
        p_score, p_name  = heapq.heappop(self.ascending)
        heapq.heappush(self.descending, (-p_score, self.rev_name(p_name)))

    def get(self) -> str:
        #print(self.ctr, "self.ctr", "len ascending", len(self.ascending))

        self.ctr += 1
        #print("ascending", self.ascending, "des", self.descending)
        p_score, p_name = heapq.heappop(self.descending)
        heapq.heappush(self.ascending, (-p_score, self.rev_name(p_name)))
        
        return p_name.replace(chr(ord('a')-1), '')
        


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()
