class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # we want to keep track of the number of current letters in a row we're looking for in the name
        # and how letters in a row we have in typed
        # if the number of letters in a row is >= the number of letters we're looking for, and the letter is the letter we're looking for,
        # keep going
        # otherwise, return False
        # cur_idx_name should be the letter right after the previous letters
        
     
        cur_name_idx = 0
        cur_ct = 1
        typed_idx = 0
        typed_ct = 0
        while cur_name_idx < len(name):
            cur_letter = name[cur_name_idx]
        
            while cur_name_idx < len(name) - 1 and name[cur_name_idx+1] == cur_letter:
                cur_name_idx += 1
                cur_ct += 1
            while typed_idx < len(typed) and typed[typed_idx] == cur_letter:
                typed_idx += 1
                typed_ct += 1
            
            if typed_ct < cur_ct:
                return False
            
            
            
            cur_name_idx += 1
            cur_ct = 1
            typed_ct = 0
        if typed_idx < len(typed):
            return False
        return True
                
