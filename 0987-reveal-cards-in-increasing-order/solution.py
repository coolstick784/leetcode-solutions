# 0 -> 2 -> 4 -> 6 -> 8 
# len(deck) = 5
# 1 -> 4 -> 

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        res = [None for _ in deck]
        deck.sort()
        next_idx = 0
        removed = set()
        for idx, n in enumerate(deck):
            res[next_idx] = n
            ctr = 0
            removed.add(next_idx)
            if idx == len(deck) - 1:
                break
            while ctr < 2:
                next_idx = (next_idx+1) % len(deck)
                if next_idx not in removed:
                    ctr += 1
               
        return res




