class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        pows = [2**n for n in range(32)][::-1]
        # Make every digit 32 bits
        # Get the sum of the differences between them
        def convertBinary(n):
            out = []
            cur_n = n
            for p in pows:
                if cur_n >= p:
                    cur_n -= p
                    out.append(1)
                else:
                    out.append(0)
            return out
                
                
                
        # 2 -> [0, 0, 0... 1, 0]
        # 1 -> [0, 0, 0 .... 1]
            
        x_arr = convertBinary(x)
        y_arr = convertBinary(y)
        
        res = sum([abs(x_arr[i] - y_arr[i]) for i in range(32)])
        
        return res 
