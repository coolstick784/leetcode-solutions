class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        

        ctr = Counter(s)
        res = ""
        idx = 0
        # If there's a match and there exists a letter after that greater than the next ch in target, roll with that and sort everything after that match
        # If there's no match and there exists a letter greater than target[0], roll with that and sort everything after that match
        # If there's a match and there doesn't exist a letter greater than target[0] after, look again after removing the previous match
        # If there doesn't exist any letter greater than the first, return ""
        if target[0] > max(ctr.keys()):
            return ""
        while idx < len(target):
            ch = target[idx]
            if ctr.get(ch, 0) > 0:
                ctr[ch] -=1
                res += ch
                idx += 1
            else:
                idx = len(target)
        


        max_char = max(["a"] +  [c for c in ctr if ctr[c] > 0])
        while res != "" and (res == target or target[len(res)] >= max_char):

            max_char = max(max_char, res[-1])
            ctr[res[-1]] += 1
            res = res[:-1]
            


        pot_to_add = [c for c in ctr if ctr[c] > 0 and c > target[len(res)]]
        if pot_to_add == []:
            return ""
        to_add = min(pot_to_add)
        res += to_add
        ctr[to_add] -=1 
        

            
        
        final = []
        for c in ctr:
            if ctr[c] > 0:
                final.extend([c for _ in range(ctr[c])])
        final.sort()
        res += "".join(final)
        return res


        
        
        
                
        
