# take each block before a reverse and a duplicate
# we'll heva a right and a left pointer
# multiply the block by the number of duplicates after it
# if it's reversed, right -= len(block) * num duplicates
# if k <= right, solve for k from there
# if it's not reversed, left += len(block) * num duplicates
# if left >= k, solve for k from there 

from collections import deque
# [1, 2, 3, 1, 2, 3]

class Solution:
    def processStr(self, s: str, k: int) -> str:
        left = 0
        right = 0
        #duplicates_after = [0 for _ in s]
        letters = set([chr(ord('a') + n) for n in range(26)])
        #reverse_after = [0 for _ in s]
        for idx, ch in enumerate(s):
            if ch == "*":
                right = max(0, right - 1)
            elif ch == "#":
                right *= 2
            elif ch in letters:
                right += 1
        # cur_dupes = 0
        # cur_rev = 0
        # for idx in range(len(s)-1, -1, -1):
        #     ch = s[idx]
            
        #     duplicates_after[idx] = cur_dupes
        #     reverse_after[idx] = cur_rev

        #     if ch == "#":
        #         cur_dupes += 1
        #     elif ch == "%":
        #         cur_rev += 1
        #         cur_rev = cur_rev % 2
        
        if k >= right or k < 0:
            return "."

        print("length", right)
        # we need to know the current length of the remaining string to the left of it
        # if we duplicate, we cut our length in half and our new goal is idx - 1/2 (length) and new length is 1/2
        # if we reverse, goal is (length-1) - idx
        # if idx == length -1 and it's a character, return it
        idx = k
        for r in range(len(s)-1, -1, -1):
            
            if r < 0:
                return -1
           
          
            if idx == right - 1 and s[r] in letters:
                return s[r]
            if s[r] in letters:
                right -= 1
                
            elif s[r] == "*":
                right += 1
                

                
            elif s[r] == "#":
                right = right // 2
                idx = idx % right
             
            elif s[r] == "%":
                idx = (right-1) - idx


        


                
        

                
                    
