from collections import Counter
class Solution:
    def longestAwesome(self, s: str) -> int:
        earliest = {}
        earliest[0] = -1
        ctr = {}
        for n in range(10):
            ctr[str(n)] = 0
        res = 0

        def get_binary(ctr):
            out = 0
            for n in range(10):
                
                if ctr[str(n)] % 2 == 1:
                    out += 2**n
            fin = []
            for n in range(10):
                
                if ctr[str(n)] % 2 == 1:
                    fin.append(out - 2 **n)
                else:
                    fin.append(out + 2 **n)
            return (out, fin)
        
        for idx, ch in enumerate(s):
            ctr[ch] = ctr.get(ch, 0) + 1
            out, cur_tuples = get_binary(ctr)
            if out not in earliest:
                earliest[out] = idx
  
            res = max(res, idx - earliest[out])
            for cur_tuple in cur_tuples:
 
                res = max(res, idx - earliest.get(cur_tuple, idx))
                
        print(earliest)
                

        return res 
