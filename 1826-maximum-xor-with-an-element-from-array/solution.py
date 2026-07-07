

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        mn = min(nums)
        mapping = {}
        nums.sort()

  
        pows = [2**n for n in range(32)]
        pows.reverse()
        for n in nums:
            cur = mapping
            for p in pows:
                if p & n:
                    val = 1
                else:
                    val = 0
                cur.setdefault(val, {})
                cur = cur[val]
                if p == 1:
                    cur['number'] = n


        res = []
        for x, m in queries:
            if m < mn:
                res.append(-1)
                continue
            m = nums[bisect.bisect(nums, m) - 1]
         
            bits = [1 if x & p else 0 for p in pows]
            m_bits = [1 if m & p else 0 for p in pows]
            is_mx = True
            cur = mapping
            n = 0
            for idx, b in enumerate(bits):
                optimal = not b
                m_bit = m_bits[idx]
           
                if is_mx and m_bit == 0:
                    options = [0]
                else:
                    options = [1, 0]
                if optimal == 0 and 0 in cur:
                
                    if is_mx and m_bit == 1:
                        is_mx = False
                    cur = cur[0]
                    
                elif optimal == 1 and 1 in options and 1 in cur:
                    n = n | pows[idx]
          
                    cur = cur[1]
                elif 0 in cur and 0 in options:
         
                    cur = cur[0]
                elif 1 in options:
                    n = n | pows[idx]
                  
                    cur = cur[1]
                else:
                    print('optimal', optimal, 'cur', cur, 'options', options)
                    break
                
            res.append(x ^ cur['number'])
        return res
                    







